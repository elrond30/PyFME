# -*- coding: utf-8 -*-
"""
Python Flight Mechanics Engine (PyFME).
Copyright (c) AeroPython Development Team.
Distributed under the terms of the MIT License.

Trimmer
-------
This module solves the problem of calculating the values of the state and
control vectors that satisfy the state equations of the aircraft at the initial
condition (or any other given condition. This cannot be done analytically
because of the very complex functional dependence of the erodynamic data.
Instead, it must be done with a numerical algorithm which iteratively adjusts
the independent variables until some solution criterion is met.
"""

from math import sqrt, sin, cos, tan, atan


def steady_state_flight_trim(aircraft, h, TAS, gamma=0, turn_rate=0):
    """Finds a combination of values of the state and control variables that
    correspond to a steady-state flight condition. Steady-state aircraft flight
    can be defined as a condition in which all of the motion variables are
    constant or zero. That is, the linear and angular velocity components are
    constant (or zero), and all acceleration components are zero.

    Parameters
    ----------
        aircraft : aircraft class
            Aircraft class with methods get_forces, get_moments
        h : float
            Geopotential altitude for ISA (m).
        TAS : float
            True Air Speed (m/s).
        gamma : float, optional
            Flight path angle (rad).
        turn_rate : float, optional
            Turn rate, d(psi)/dt (rad/s).

    Returns
    -------
        lin_vel :

        ang_vel :

        theta :

        phi :

        alpha :

        beta :

        control_vector :


    Notes
    -----
    See section 3.4 in [1] for the algorithm description.
    See section 2.5 in [1] for the definition of steady-state flight condition.

    References
    ----------
    .. [1] Stevens, BL and Lewis, FL, "Aircraft Control and Simulation",
        Wiley-lnterscience.
    """

    pass

    return


def turn_coord_cons1(turn_rate, alpha, beta, TAS, gamma=0):
    """Calculates phi for coordinated turn
    """

    g0 = 9.8
    G = turn_rate * TAS / g0

    if gamma == 0:
        phi = G * cos(beta) / (cos(alpha) - G * sin(alpha) * sin(beta))
        phi = atan(phi)

    else:
        a = 1 - G * tan(alpha) * sin(beta)
        b = sin(gamma) / cos(beta)
        c = 1 + G**2 * cos(beta)**2

        sq = sqrt(c * (1 - b**2) + G**2 * sin(beta)**2)
        var1 = b**2 * (1 + c * tan(alpha)**2)

        temp = (a - b)**2 + b * tan(alpha) * sq / a**2 - b**2 * var1

        phi = atan(G * cos(beta) / cos(alpha) * temp)

    return phi


def turn_coord_cons2(turn_rate, alpha, TAS):
    """Calculates phi for coordinated given that gamma is equal to cero and
    beta is small (beta << 1).
    """

    g0 = 9.8
    G = turn_rate * TAS / g0

    phi = G / cos(alpha)

    return phi


def rate_of_climb_cons(gamma, alpha, beta, phi):
    """
    """
    a = cos(alpha) * cos(beta)
    b = sin(phi) * sin(beta) + cos(phi) * sin(alpha) * cos(beta)

    sq = sqrt(a**2 - sin(gamma)**2 + b**2)

    theta = (a * b + sin(gamma) * sq) / (a**2 - sin(gamma)**2)
    theta = atan(theta)

    return theta
