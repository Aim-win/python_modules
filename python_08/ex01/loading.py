import importlib
from typing import Any


def check_dependency(package_name: str) -> str:
    """Check if a package is installed and return its version status."""
    package_message = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    try:
        module = importlib.import_module(package_name)
        return (f"[OK] {package_name} ({module.__version__})"
                f" - {package_message[package_name]}")
    except ImportError:
        return f"[KO] {package_name} not found"


def analyze_data() -> Any:
    """Generate 1000-point Matrix signal data using numpy
             and return a DataFrame."""
    print("Analyzing Matrix data...")
    try:
        print("Processing 1000 data points...")
        import pandas
        import numpy

        data = {
            "time": numpy.arange(1000),
            "signal": numpy.random.randn(1000)
        }
        return pandas.DataFrame(data)
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None


def create_visualization(data: Any) -> None:
    """Plot the Matrix signal data and save it as a PNG file."""
    try:
        import matplotlib.pyplot as plt

        print("Generating visualization...\n")
        plt.plot(data["time"], data["signal"])
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(f"Error during visualization: {e}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    dependencies = ["pandas", "numpy", "requests", "matplotlib"]
    check_flag = True

    for dependency in dependencies:
        val = check_dependency(dependency)
        if "[KO]" in val:
            check_flag = False
        print(val)

    if check_flag:
        print()
        data = analyze_data()
        create_visualization(data)
    else:
        print("\nNothing To Analyse !")
