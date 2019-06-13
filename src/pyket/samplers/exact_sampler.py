import numpy

from pyket.deepar.samplers.base_sampler import Sampler
from ..exact.utils import decimal_array_to_binary_array


class ExactSampler(Sampler):
    """docstring for Sampler"""

    def __init__(self, exact_variational, batch_size, **kwargs):
        super(ExactSampler, self).__init__(exact_variational.input_size, batch_size, **kwargs)
        self.exact_variational = exact_variational

    def __next__(self):
        decimal_batch = numpy.random.choice(self.exact_variational.num_of_states,
                                            size=self.batch_size,
                                            p=self.exact_variational.probs)
        binary_batch = decimal_array_to_binary_array(decimal_batch,
                                                     num_of_bits=self.exact_variational.number_of_spins)
        return binary_batch.reshape((self.batch_size,) + self.input_size)
