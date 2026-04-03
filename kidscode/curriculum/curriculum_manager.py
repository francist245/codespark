"""
Curriculum Manager - Loads, indexes, and provides lessons for each profile.
"""
from typing import Optional


class CurriculumManager:
    def __init__(self):
        self._modules = {}   # profile -> list of module dicts
        self._lessons = {}   # lesson_id -> lesson dict
        self._load_all()

    def _load_all(self):
        from kidscode.curriculum.joshua_curriculum import JOSHUA_MODULES
        from kidscode.curriculum.toby_curriculum import TOBY_MODULES

        self._modules['joshua'] = JOSHUA_MODULES
        self._modules['toby'] = TOBY_MODULES

        # Index all lessons by id
        for profile_modules in [JOSHUA_MODULES, TOBY_MODULES]:
            for module in profile_modules:
                for lesson in module.get('lessons', []):
                    self._lessons[lesson['id']] = lesson

    # ------------------------------------------------------------------
    # Access helpers
    # ------------------------------------------------------------------

    def get_modules(self, profile: str) -> list:
        """Return all modules for a profile (ordered)."""
        return self._modules.get(profile, [])

    def get_lesson(self, lesson_id: str) -> Optional[dict]:
        return self._lessons.get(lesson_id)

    def get_module_by_id(self, profile: str, module_id: str) -> Optional[dict]:
        for m in self._modules.get(profile, []):
            if m['id'] == module_id:
                return m
        return None

    def all_lesson_ids(self, profile: str) -> list:
        ids = []
        for m in self._modules.get(profile, []):
            ids.extend(l['id'] for l in m.get('lessons', []))
        return ids

    def next_lesson(self, profile: str, current_lesson_id: str) -> Optional[dict]:
        """Return the next lesson after current_lesson_id, or None."""
        ids = self.all_lesson_ids(profile)
        try:
            idx = ids.index(current_lesson_id)
            if idx + 1 < len(ids):
                return self._lessons[ids[idx + 1]]
        except ValueError:
            pass
        return None
