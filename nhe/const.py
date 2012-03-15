"""
Module :mod:`nhe.const` defines various constants.
"""


class ConstantContainer(object):
    """
    Class that doesn't support instantiation.

    >>> ConstantContainer()
    Traceback (most recent call last):
        ...
    AssertionError: do not create objects ConstantContainer, \
use class properties instead
    """
    def __init__(self):
        raise AssertionError('do not create objects %s, '
                             'use class properties instead'
                             % type(self).__name__)


class TRT(ConstantContainer):
    """
    Container for constants that define Tectonic Region Types.
    """
    # Constant values correspond to the NRML schema definition.
    ACTIVE_SHALLOW_CRUST = 'Active Shallow Crust'
    STABLE_CONTINENTAL = 'Stable Shallow Crust'
    SUBDUCTION_INTERFACE = 'Subduction Interface'
    SUBDUCTION_INTRASLAB = 'Subduction IntraSlab'
    VOLCANIC = 'Volcanic'

    ALL = set((ACTIVE_SHALLOW_CRUST, STABLE_CONTINENTAL,
               SUBDUCTION_INTERFACE, SUBDUCTION_INTRASLAB,
               VOLCANIC))

    @classmethod
    def is_valid(cls, value):
        """
        Return ``True`` if ``value`` references a correct tectonic region type.

        >>> TRT.is_valid('Active Shallow Crust')
        True
        >>> TRT.is_valid('Active Shallo Crust')
        False
        """
        return value in cls.ALL


class IMC(ConstantContainer):
    """
    The intensity measure component is the component of interest
    of ground shaking for an :mod:`intensity measure <nhe.imt>`.
    """
    #: Usually defined as the geometric average of the maximum
    #: of the two horizontal components (which may not occur
    #: at the same time).
    AVERAGE_HORIZONTAL = 'Average horizontal'
    #: An orientation-independent alternative to :attr:`AVERAGE_HORIZONTAL`.
    #: Defined at Boore et al. (2006, Bull. Seism. Soc. Am. 96, 1502-1511)
    #: and is used for all the NGA GMPEs.
    GMRotI50 = 'Average Horizontal (GMRotI50)'
    #: A randomly chosen horizontal component.
    RANDOM_HORIZONTAL = 'Random horizontal'
    #: The largest value obtained from two perpendicular horizontal
    #: components.
    GREATER_OF_TWO_HORIZONTAL = 'Greater of two horizontal'
    #: The vertical component.
    VERTICAL = 'Vertical'


class StdDev(ConstantContainer):
    """
    GSIM standard deviation represents ground shaking variability at a site.
    """
    #: Standard deviation representing ground shaking variability
    #: within different events.
    INTER_EVENT = 'Inter event'
    #: Standard deviation representing ground shaking variability
    #: within a single event.
    INTRA_EVENT = 'Intra event'
    #: Total standard deviation, defined as the square root of the sum
    #: of inter- and intra-event squared standard deviations, represents
    #: the total ground shaking variability, and is the only one that
    #: is used for calculating a probability of intensity exceedance
    #: (see :meth:`nhe.gsim.base.GroundShakingIntensityModel.get_poes`).
    TOTAL = 'Total'