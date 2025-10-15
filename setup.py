from setuptools import setup, find_packages

setup(
    name="vnstock_chart",
    version="1.0.0",
    author="vnstock-hq",
    author_email="support@vnstocks.com",
    description="Professional financial charting library for Python. Supports backtesting, performance analytics, dashboards, and TradingView/Bloomberg-style visualizations.",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "pyecharts>=2.0.0",
        "jupyter_bokeh>=3.0.0",
        "panel>=1.8.2"
    ],
    extras_require={"dev": ["pytest", "pytest-cov"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: User Interfaces",
        "Natural Language :: English",
        "Development Status :: 4 - Beta"
    ],
)
