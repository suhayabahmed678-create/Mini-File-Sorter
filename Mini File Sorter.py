from pathlib import Path

# ------------------------------
# Optional Utilities
# ------------------------------
try:
    from utils.config_manager import ConfigManager
    BASE_PATH = getattr(ConfigManager, "SCAN_PATH", Path("."))
except Exception:
    BASE_PATH = Path(".")


def log(msg):
    print(f"[LOG] {msg}")


# ------------------------------
# Extension Map
# ------------------------------
EXTENSION_MAP = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".mp4": "Videos", ".avi": "Videos",
    ".mp3": "Audio", ".wav": "Audio",
    ".txt": "Docs", ".pdf": "Docs",
    ".py": "Code", ".js": "Code", ".html": "Code"
}


# ------------------------------
# Core Engine
# ------------------------------
class MiniSorter:

    def __init__(self, folder: Path):
        self.folder = folder
        self.bucket = {}

    def _get_group(self, suffix: str):
        return EXTENSION_MAP.get(suffix.lower(), "Misc")

    def analyze_files(self):
        log(f"Analyzing → {self.folder}")

        if not self.folder.exists():
            print("Folder not found.")
            return

        for f in self.folder.glob("*"):
            if f.is_file():
                group = self._get_group(f.suffix)

                if group not in self.bucket:
                    self.bucket[group] = []

                self.bucket[group].append(f.name)

        log("Analysis done.")

    def show_summary(self):
        print("\n==== File Summary ====\n")

        if not self.bucket:
            print("No bucket found.")
            return

        for group in sorted(self.bucket):
            files = self.bucket[group]
            print(f"[{group}] → {len(files)} item(s)")
            for name in files:
                print("   •", name)
            print()


# ------------------------------
# Entry Point
# ------------------------------
def main():
    sorter = MiniSorter(Path(BASE_PATH))
    sorter.analyze_files()
    sorter.show_summary()


if __name__ == "__main__":
    main()



