# bisbislib
研究用ライブラリ

## unittest

### テストファイルの作成

- `generate__init__.py`を実行することで、以下の手順が自動的に行われる

1. `test`ディレクトリ下に、`bisbislib`ディレクトリ下に対応させたディレクトリ構成でファイルを作成する
   - ファイル名には`test_`をプレフィックスとして付与
   - e.g. `bisbislib/hoge/fuga.py`に対応するテストファイルは`test/hoge/test_fuga.py`
2. 新たにディレクトリを作成した場合は、空の`__init__.py`ファイルを配置する

### テストファイルのテンプレート

```python
import unittest

from bisbislib.xxx import xxx


class TestXxx(unittest.TestCase):
    def test_xxx(self):
        pass
```

### テストの実行

```sh
python -m unittest
```
