"""
Representer for Python.
"""
import ast
import astor

from .transformer import RepresenterTransformer
from .utils import Slug, Directory, reformat, to_json


def represent(exercise: Slug, path: Directory) -> None:

    src = path.joinpath(exercise.replace("-", "_") + ".py")

    transformer = RepresenterTransformer()

    tree = ast.parse(src.read_text())
    print(astor.dump_tree(tree, indentation="  ", maxline=88))

    tree = transformer.visit(tree)
    print(astor.dump_tree(tree, indentation="  ", maxline=88))

    representation = reformat(astor.to_source(tree))
    dst = path.joinpath("representation.txt")
    dst.write_text(representation)

    mapping = to_json(transformer.get_placeholders())
    dst = path.joinpath("mapping.json")
    dst.write_text(mapping)
