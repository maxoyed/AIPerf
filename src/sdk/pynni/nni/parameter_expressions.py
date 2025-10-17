# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

'''
parameter_expression.py
'''

from __future__ import annotations

try:
    import numpy as np
except ModuleNotFoundError:  # pragma: no cover - optional dependency in tests
    np = None  # type: ignore[assignment]


def _require_numpy() -> None:
    """Raise a helpful error when ``numpy`` is unavailable."""
    if np is None:  # type: ignore[truthy-bool]
        raise RuntimeError(
            "NumPy is required for sampling parameter expressions. "
            "Install the optional dependency or skip tests that rely on it."
        )


def choice(options, random_state):
    '''
    options: 1-D array-like or int
    random_state: an object of numpy.random.RandomState
    '''
    return random_state.choice(options)


def randint(lower, upper, random_state):
    '''
    Generate a random integer from `lower` (inclusive) to `upper` (exclusive).
    lower: an int that represent an lower bound
    upper: an int that represent an upper bound
    random_state: an object of numpy.random.RandomState
    '''
    return random_state.randint(lower, upper)


def uniform(low, high, random_state):
    '''
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    random_state: an object of numpy.random.RandomState
    '''
    assert high >= low, 'Upper bound must be larger than lower bound'
    return random_state.uniform(low, high)


def quniform(low, high, q, random_state):
    '''
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    q: sample step
    random_state: an object of numpy.random.RandomState
    '''
    _require_numpy()
    return np.clip(np.round(uniform(low, high, random_state) / q) * q, low, high)  # type: ignore[arg-type]


def loguniform(low, high, random_state):
    '''
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    random_state: an object of numpy.random.RandomState
    '''
    assert low > 0, 'Lower bound must be positive'
    _require_numpy()
    return np.exp(uniform(np.log(low), np.log(high), random_state))  # type: ignore[arg-type]


def qloguniform(low, high, q, random_state):
    '''
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    q: sample step
    random_state: an object of numpy.random.RandomState
    '''
    _require_numpy()
    return np.clip(np.round(loguniform(low, high, random_state) / q) * q, low, high)  # type: ignore[arg-type]


def normal(mu, sigma, random_state):
    '''
    The probability density function of the normal distribution,
    first derived by De Moivre and 200 years later by both Gauss and Laplace independently.
    mu: float or array_like of floats
        Mean (“centre”) of the distribution.
    sigma: float or array_like of floats
           Standard deviation (spread or “width”) of the distribution.
    random_state: an object of numpy.random.RandomState
    '''
    return random_state.normal(mu, sigma)


def qnormal(mu, sigma, q, random_state):
    '''
    mu: float or array_like of floats
    sigma: float or array_like of floats
    q: sample step
    random_state: an object of numpy.random.RandomState
    '''
    _require_numpy()
    return np.round(normal(mu, sigma, random_state) / q) * q  # type: ignore[arg-type]


def lognormal(mu, sigma, random_state):
    '''
    mu: float or array_like of floats
    sigma: float or array_like of floats
    random_state: an object of numpy.random.RandomState
    '''
    _require_numpy()
    return np.exp(normal(mu, sigma, random_state))  # type: ignore[arg-type]


def qlognormal(mu, sigma, q, random_state):
    '''
    mu: float or array_like of floats
    sigma: float or array_like of floats
    q: sample step
    random_state: an object of numpy.random.RandomState
    '''
    _require_numpy()
    return np.round(lognormal(mu, sigma, random_state) / q) * q  # type: ignore[arg-type]
