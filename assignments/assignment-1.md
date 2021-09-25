# ANLY-580 Assignment 1

The purpose of this assignment is to familiarize you with some of the underlying concepts used in machine learning and NLP. Feel free to use definitions from Wikipedia to aid in this self study, but refrain from searching for answers directly. If you get stuck, team up with no more than three classmates and work together. If you work in teams, please list your teammates on your submission.

To submit this assignment, either enter your answers directly in the `assignments/assignment-1.md` using markdown syntax, or upload a separate file containing your solutions, for example `assignments/assignment-1-solutions.pdf`.

*Note: You will need to complete the [Github onboarding instructions](https://github.com/chrislarson1/GU-ANLY-580-FALL-2021/blob/main/github-setup.md) in order to submit this assignment.*

#
**Format**: take home, open Wikipedia, groups of $\leq$ 3

**Due dates**:
 
 - Section I: Sep 26
 - Section II: Sep 26

**Grade**: 10% (100 pts)

**Your name**:

**Your NET ID**:

#
## Problems

1. (10 pts) Establish the [convexity](https://en.wikipedia.org/wiki/Convex_function) of the following functions, showing any necessary derivation steps.

    a. $f(x) = x^{2}$
    
       $f'(x) = {2}x$
       
       $f"(x) = {2}$
       
       $2 > 0$, therefore f(x) is always Concave Up (Concave Up on the set of all real numbers)

    b. $f(x) = \ln(x)$
    
       $f'(x) = \frac{1}{x}$
       
       $f"(x) = \frac{-1}{x^{2}}$
       
       $\frac{-1}{x^{2}} < 0$ when x > 0, therefore f(x) is Concave Down on the set of x > 0 (ln(x) only exists in the domain x > 0)

    c. $f(x) = \frac{1}{1 + e^{-x}}$
       
       $f'(x) = -\frac{1}{1 + e^{-x}} * e^{-x} * -{1}$
       
       $f'(x) = \frac{e^{-x}}{1 + e^{-x}}$
       
       $f"(x) = -e^{-x} * f(x) + e^{-x} * f'(x)$
       
       $f"(x) = f'(x) * (-{1} + e^{-x})$
       
       $f"(x) = \frac{e^{-x}(e^{-x}-{1})}{{1} + e^{-x}}$
       
       When $e^{-x} < {1}$, f"(x) < 0, and the f(x) is Concave Down. When $e^{-x} > {1}$, f(x) is Concave Up (inflection when e^{-x} == 1)

    *Hint: convexity is non binary, some functions are neither convex nor concave, some are convex/concave over finite intervals etc..* 



2. (10 pts) Consider a continuous random variable $X$ that is drawn from a [uniform distribution](https://en.wikipedia.org/wiki/Continuous_uniform_distribution) between the values $0$ and $\theta$. Please compute the following, showing each derivation step:

    a. $\mathbb{E}_{X}[X]$
       $\mathbb{E}_{X}[X]$ = Expected Value of X. f(x) = {$\frac{{1}/{\theta}$ for 0 <= x <= $\theta$, 0 everywhere else}
       $\mathbb{E}_{X}[X]$ = Integral of x * f(x)dx from 0 to $\theta$ = Integral of $\frac{{x * dx}{\theta}} = \frac{{x^{2}}{{2} * \theta}}$ from 0 to $\theta$ = $\frac{{\theta^{2}}{{2} * \theta}} = \frac{{\theta}{{2}}}$

    b. $\text{var}(X)$
       $\text{var}(X) = \mathbb{E}_{X^2}[X^2] - \mathbb{E}_{X}[X]$
       $\mathbb{E}_{X^2}[X^2] = $ Integral of x^2 * f(x)dx from 0 to $\theta$ = Integral of $\frac{{x^{2} * dx}{\theta}} = \frac{{x^{3}}{{3} * \theta}}$ from 0 to $\theta$ = $\frac{{\theta^{3}}{{3} * \theta}} = \frac{{\theta^{2}}{3}}$
       $\mathbb{E}_{X}[X] = \frac{{\theta}{{2}}}$ (Above)
       $\text{var}(X) = \frac{{\theta^{2}}{3}} - \frac{{\theta}{{2}}}$

    c. $H(X)$

    *Note:* $H(X)$ *denotes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of* $X$. 


3. (40 pts) Given $M$ independently drawn samples of $X$ from (2), $x_{1}, ..., x_{M}$, compute the [maximum likelihood estimate](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) of $\theta$, $\hat{\theta}$. Please show the steps to arrive at this answer.


3. (20 pts) Imagine you are given the choice of three sound proof doors: Behind one door is \$1M cash; behind the others, crickets. After making your choice (but not observing the outcome), an omnicient host reveals crickets behind one of the other doors. The host then asks you the following: *Would you like to switch doors?* Using [Bayes' Rule](https://en.wikipedia.org/wiki/Bayes%27_theorem), determine whether or not you should switch doors to maximize your chances of winning $1M.


4. (20 pts) Consider the covariance matrix, $\Sigma \in \mathbb{R}^{N \times N}$ of a random vector $X \in \mathbb{R}^{N}$. Show that $\Sigma$ is a [positive semidefnite matrix](https://en.wikipedia.org/wiki/Definite_matrix). What are some of the implications of $\Sigma$ being PSD?

    *Note: The covariance of $X$ is defined as $\Sigma = \mathbb{E}_{X}\big[ \big( X - \mathbb{E}_{X}[X] \big)\big( X - \mathbb{E}_{X}[X] \big)^{T} \big]$*
