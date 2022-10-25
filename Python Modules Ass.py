{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.23606797749979\n"
     ]
    }
   ],
   "source": [
    "# 1.\n",
    "import math, random\n",
    "print(math.sqrt(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Provide three examples using the ** random ** submodule in ** numpy ** module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([18,  4, 25,  4, 27])"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from numpy import random\n",
    "x = random.randint(1, 30, 5)\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[37 39 42 21]\n"
     ]
    }
   ],
   "source": [
    "x = random.randint(2, 20, 4)\n",
    "y = random.randint(2, 40, 4)\n",
    "print(x + y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0.66111343, 0.61904756, 0.53563114, 0.44167872, 0.94831643,\n",
       "       0.50329601, 0.95331204, 0.2886494 , 0.0812153 , 0.03875815])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = random.random(10)\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a function to generate three random numbers with the numpy module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([ 5, 17, 11, 13]), array([8, 9, 4, 2]))\n"
     ]
    }
   ],
   "source": [
    "random.seed(20)\n",
    "def get_random(age1, age2):\n",
    "    return age1, age2\n",
    "age1 = random.randint(2, 20, 4)\n",
    "age2 = random.randint(2, 13, 4)\n",
    "result = get_random(age1, age2)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
