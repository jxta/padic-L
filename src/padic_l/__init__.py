"""
p進L関数と素数分布論研究プロジェクト

このパッケージは、p進L関数の符号変化パターンと古典的Chebyshev偏りの
相関を数値実験により解明し、「p進素数分布論」という新しい数学分野の
基礎を構築することを目的としています。

主要モジュール:
- core: p進L関数の核心計算
- iwasawa: 岩澤理論的解析
- classical: 古典的素数分布計算
- utils: ユーティリティ関数群
"""

__version__ = "0.1.0"
__author__ = "青木美穂, プロジェクトチーム"
__email__ = "research-team@padic-l.org"

# 主要クラスのインポート
from .core.padic_l_function import PadicLFunction
from .core.dirichlet_chars import DirichletCharacterAnalyzer
from .classical.bias_computation import ClassicalBiasComputer
from .utils.parallel import ParallelComputation

__all__ = [
    "PadicLFunction",
    "DirichletCharacterAnalyzer", 
    "ClassicalBiasComputer",
    "ParallelComputation",
]