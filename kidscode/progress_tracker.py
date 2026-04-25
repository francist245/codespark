"""
Progress Tracker - Saves and loads per-profile learning progress.
Data stored in: ~/KidsCode/data/progress.json
"""
import copy
import json
import os
from pathlib import Path
from datetime import datetime


DATA_DIR = Path.home() / 'KidsCode' / 'data'
PROGRESS_FILE = DATA_DIR / 'progress.json'


def _now() -> str:
    return datetime.now().isoformat(timespec='seconds')


DEFAULT_PROFILE = {
    'completed_lessons': [],      # list of lesson IDs
    'quiz_scores': {},            # lesson_id -> score (0-100)
    'total_xp': 0,
    'badges': [],                 # list of badge names earned
    'streak_days': 0,
    'last_session': None,
    'sessions': 0,
    'created_at': None,
}


class ProgressTracker:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self._data = self._load()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> dict:
        if PROGRESS_FILE.exists():
            try:
                with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return {'joshua': copy.deepcopy(DEFAULT_PROFILE), 'toby': copy.deepcopy(DEFAULT_PROFILE)}

    def save(self):
        try:
            with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, indent=2)
        except OSError as e:
            print(f"Warning: Could not save progress: {e}")

    def _profile(self, profile: str) -> dict:
        if profile not in self._data:
            self._data[profile] = copy.deepcopy(DEFAULT_PROFILE)
        p = self._data[profile]
        # Back-fill any missing keys from DEFAULT_PROFILE
        for k, v in DEFAULT_PROFILE.items():
            if k not in p:
                p[k] = copy.deepcopy(v)
        return p

    # ------------------------------------------------------------------
    # Session tracking
    # ------------------------------------------------------------------

    def start_session(self, profile: str):
        p = self._profile(profile)
        p['sessions'] += 1
        if not p['created_at']:
            p['created_at'] = _now()

        # Streak calculation
        today = datetime.now().date()
        last = p.get('last_session')
        if last:
            try:
                last_date = datetime.fromisoformat(last).date()
                delta = (today - last_date).days
                if delta == 0:
                    # Same day — ensure streak is at least 1
                    if p.get('streak_days', 0) == 0:
                        p['streak_days'] = 1
                elif delta == 1:
                    p['streak_days'] = p.get('streak_days', 0) + 1  # consecutive day!
                else:
                    p['streak_days'] = 1  # streak broken, reset
            except (ValueError, TypeError):
                p['streak_days'] = 1
        else:
            p['streak_days'] = 1  # first ever session

        p['last_session'] = _now()
        self.save()

    def get_streak(self, profile: str) -> int:
        return self._profile(profile).get('streak_days', 0)

    def get_display_name(self, profile: str) -> str:
        """Return a display-friendly name for the profile."""
        names = {'joshua': 'Joshua', 'toby': 'Toby'}
        return names.get(profile.lower(), profile.capitalize())

    # ------------------------------------------------------------------
    # Lesson completion
    # ------------------------------------------------------------------

    def is_lesson_complete(self, profile: str, lesson_id: str) -> bool:
        return lesson_id in self._profile(profile)['completed_lessons']

    def complete_lesson(self, profile: str, lesson_id: str, xp: int = 50, quiz_score: int = None):
        # Guard: reject cross-profile lesson IDs (j_ prefix for joshua, t_ for toby)
        expected_prefix = 'j_' if profile == 'joshua' else 't_'
        if not lesson_id.startswith(expected_prefix):
            return
        p = self._profile(profile)
        if lesson_id not in p['completed_lessons']:
            p['completed_lessons'].append(lesson_id)
            p['total_xp'] += xp
        if quiz_score is not None:
            p['quiz_scores'][lesson_id] = quiz_score
        self.save()

    def record_quiz_score(self, profile: str, lesson_id: str, step_title: str, correct: bool):
        """Record an individual quiz answer result."""
        p = self._profile(profile)
        key = f"{lesson_id}::{step_title}"
        p['quiz_scores'][key] = 'correct' if correct else 'incorrect'
        self.save()

    def get_completed_lessons(self, profile: str) -> list:
        return list(self._profile(profile)['completed_lessons'])

    # ------------------------------------------------------------------
    # XP and Level
    # ------------------------------------------------------------------

    def get_xp(self, profile: str) -> int:
        return self._profile(profile)['total_xp']

    def get_level(self, profile: str) -> int:
        """Level = XP // 200  (levels start at 1)."""
        return max(1, self.get_xp(profile) // 200 + 1)

    def get_xp_to_next_level(self, profile: str) -> tuple:
        """Return (current_xp_in_level, xp_needed_for_level)."""
        xp = self.get_xp(profile)
        level_xp = xp % 200
        return level_xp, 200

    # ------------------------------------------------------------------
    # Stars (used in Joshua's UI)
    # ------------------------------------------------------------------

    def get_stars(self, profile: str) -> int:
        """Stars = 1 per completed lesson."""
        return len(self.get_completed_lessons(profile))

    # ------------------------------------------------------------------
    # Badges
    # ------------------------------------------------------------------

    def award_badge(self, profile: str, badge_name: str):
        p = self._profile(profile)
        if badge_name not in p['badges']:
            p['badges'].append(badge_name)
            self.save()
            return True
        return False

    def has_badge(self, profile: str, badge_name: str) -> bool:
        return badge_name in self._profile(profile).get('badges', [])

    def get_badges(self, profile: str) -> list:
        return list(self._profile(profile).get('badges', []))

    # ------------------------------------------------------------------
    # Module progress helpers
    # ------------------------------------------------------------------

    def get_module_progress(self, profile: str, module_lesson_ids: list) -> tuple:
        """Return (completed_count, total_count) for a module."""
        completed = self.get_completed_lessons(profile)
        done = sum(1 for lid in module_lesson_ids if lid in completed)
        return done, len(module_lesson_ids)

    def is_module_unlocked(self, profile: str, prerequisite_lesson_ids: list) -> bool:
        """A module is unlocked if all prerequisite lessons are complete."""
        if not prerequisite_lesson_ids:
            return True
        completed = self.get_completed_lessons(profile)
        return all(lid in completed for lid in prerequisite_lesson_ids)
