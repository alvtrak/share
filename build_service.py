import dataclasses
from typing import List


@dataclasses.dataclass
class Step:
    """A step in a build.

    Attributes:
        name: the name of the step.
        dependencies: the step names this step depends on.
    """

    name: str
    dependencies: List[str]


class BuildService:
    """Stores steps and their dependencies for a given build.

    For example, each of the following is a step in a build and the steps it depends on.

    | Step Name   | Dependencies |
    |-------------|--------------|
    | A           |              |
    | B           | A            |
    | C           | A            |
    | D           | A            |
    | E           | B, D, C      |
    | F           | E            |

    Given the above, `A -> B -> C -> D -> E -> F` would be a valid order to run the build steps.
    """

    def __init__(self, steps: List[Step]):
        raise NotImplementedError("TODO")

    def is_direct_dependency(self, step: str, maybe_dependency: str) -> bool:
        """Checks if a step is a direct dependency of another step

        For example, given steps A <- B <- C
            * "A" is a direct dependency of "B" (B depends on A)
            * "A" is not a direct dependency of "C" (C depends on B depends on A)
            * "B" is a direct dependency of "C" (B depends on C)

        Args:
            step: a build step
            maybe_dependency: another build step

        Returns:
            True if the `maybe_dependency` is a direct dependency for the `step`, else False.
        """
        raise NotImplementedError("TODO")


def main():
    build_steps = [
        Step("A", []),
        Step("B", ["A"]),
        Step("C", ["A"]),
        Step("D", ["A"]),
        Step("E", ["B", "C", "D"]),
        Step("F", ["E"]),
    ]

    build = BuildService(build_steps)
    print(f"A is a dependency of B: {build.is_direct_dependency('B', 'A')}")  # true
    print(f"B is a dependency of A: {build.is_direct_dependency('A', 'B')}")  # false


if __name__ == "__main__":
    main()