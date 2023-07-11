"""__init__.py を自動生成するプログラム（1行の最大文字数には非対応）"""
import re
from pathlib import Path
from typing import Dict, List


def listup_files(target_path: Path) -> Dict[str, List[str]]:
    """__init__.py を除く Python ファイルを抽出

    Args:
        target_path (Path): 探索対象パス

    Returns:
        Dict[str, List[str]]:
            keyをディレクトリパス、valueをファイル名のリストとした辞書
    """
    target_file_list: Dict[str, List[str]] = {}

    for path in target_path.glob("**"):
        if not path.is_dir():
            continue

        for file in path.glob("*.py"):
            if not file.is_file():
                continue
            if file.name == "__init__.py":
                continue

            if str(file.parent) in target_file_list:
                target_file_list[str(file.parent)].append(str(file.name))
            else:
                target_file_list[str(file.parent)] = [str(file.name)]

    return target_file_list


def explore_modules(
    target_file_list: Dict[str, List[str]]
) -> Dict[str, Dict[str, List[str]]]:
    """ファイル内で定義されているクラスと関数の名前を抽出

    Args:
        target_file_list (Dict[str, List[str]]):
            listup_files()で抽出された対象ファイルのリストの辞書

    Returns:
        Dict[str, Dict[str, List[str]]]:
            keyをディレクトリパスおよびファイルベースネーム、
            valueをクラス名または関数名とした辞書
    """
    module_list: Dict[str, Dict[str, List[str]]] = {}

    for dir_name, file_list in target_file_list.items():
        for file in sorted(file_list):
            with open(Path(dir_name) / file, "r") as f:
                lines = f.readlines()

            for line in lines:
                match = re.match(r"(class|def) (.+?)[\(:]", line)
                if match:
                    module_name = match.group(2)
                    file_stem = Path(file).stem

                    if dir_name not in module_list:
                        module_list[dir_name] = {}
                    if file_stem not in module_list[dir_name]:
                        module_list[dir_name][file_stem] = []
                    module_list[dir_name][file_stem].append(module_name)

    return module_list


def generate_init_file(module_list: Dict[str, Dict[str, List[str]]]) -> None:
    """各ディレクトリに __init__.py ファイルを生成

    Args:
        module_list (Dict[str, Dict[str, List[str]]]):
            explore_modules()で抽出されたクラス名および関数名の辞書
    """
    for dir_name, file_dict in module_list.items():
        import_list = []
        all_list = []
        for file_name, module_name_list in file_dict.items():
            module_name = ", ".join(module_name_list)
            import_list.append(f"from .{file_name} import {module_name}")
            all_list.extend(module_name_list)

        with open(Path(dir_name) / "__init__.py", "w") as f:
            import_text = "\n".join(import_list)
            all_text = '"' + '", "'.join(all_list) + '"'
            f.write(f"{import_text}\n")
            f.write("\n")
            f.write(f"__all__ = [{all_text}]\n")


def generate_empty_init_file(target_path: Path) -> None:
    """空の__init__.pyを再帰的に生成

    Args:
        target_path (Path): 探索対象パス
    """
    for path in target_path.glob("**"):
        if path.is_dir():
            path_init = path / "__init__.py"
            if not path_init.exists():
                path_init.touch()


if __name__ == "__main__":
    target_path = Path("bisbislib")
    target_file_list = listup_files(target_path)
    module_list = explore_modules(target_file_list)
    generate_init_file(module_list)
    generate_empty_init_file(target_path)

    target_path = Path("test")
    generate_empty_init_file(target_path)
