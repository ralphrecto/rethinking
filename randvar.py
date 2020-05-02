{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "__all__ = [\n",
    "    \"uniform\",\n",
    "    \"normal\"\n",
    "]\n",
    "\n",
    "class RandVar:\n",
    "    \n",
    "    def __init__(self, sampler):\n",
    "        self.sampler = sampler\n",
    "        \n",
    "    def sample(self, num):\n",
    "        return self.sampler(num)\n",
    "    \n",
    "    def sample_series(self, num):\n",
    "        return pd.Series(self.sample(num))\n",
    "    \n",
    "\n",
    "def papply(f, *args):\n",
    "    return lambda x: f(*args, x)\n",
    "\n",
    "def const(c):\n",
    "    return RandVar(lambda num: np.full(num, c))\n",
    "\n",
    "def randvar(c):\n",
    "    if isinstance(c, RandVar):\n",
    "        return c\n",
    "    else:\n",
    "        return const(c)\n",
    "\n",
    "def uniform(low, high):\n",
    "    low_r = randvar(low)\n",
    "    high_r = randvar(high)\n",
    "    \n",
    "    def sampler(num):\n",
    "        low_samples = low_r.sample(num)\n",
    "        high_samples = high_r.sample(num)\n",
    "        return np.random.uniform(low_samples, high_samples)\n",
    "        \n",
    "    return RandVar(sampler)\n",
    "\n",
    "def normal(mu, sigma):\n",
    "    mu_r = randvar(mu)\n",
    "    sigma_r = randvar(sigma)\n",
    "    \n",
    "    def sampler(num):\n",
    "        mu_samples = mu_r.sample(num)\n",
    "        sigma_samples = sigma_r.sample(num)\n",
    "        return np.random.normal(mu_samples, sigma_samples)\n",
    "    \n",
    "    return RandVar(sampler)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
