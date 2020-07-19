#Nimish Verma
import numpy as np

from ..util.base_visualizer import BaseVisualizer

class Visualizer(BaseVisualizer):

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #
    #     ax = self._fig.gca(label='BaseAxis')
    #     self.__alpha_wolf_artist, = ax.plot([], [], 'o', color='#FFA500' if self._dark else '#ffff00', ms=6)
    #     self.__alpha_wolf = [[], []]
    #
    #     self.__beta_wolf_artist, = ax.plot([], [], 'o', color='#b60909' if self._dark else '#6d0505', ms=6)
    #     self.__beta_wolf = [[], []]
    #
    #     self.__delta_wolf_artist, = ax.plot([], [], 'o', color='#295721' if self._dark else '#53af42', ms=6)
    #     self.__delta_wolf = [[], []]
    #
    #     # self.__omega_positions = []
    #     # self.__omegas_artist, = ax.plot([], [], 'o', color='darkblue' if self._dark else 'blue', ms=6)
    #
    #

    def replay(self):
        # Prepare velocities before starting replay
        self._velocities = [self._positions[index+1]-position for index, position in enumerate(self._positions[:-1])]
        self._velocities.insert(0, np.zeros(self._positions[0].shape))
        self._velocities.append(np.zeros(self._positions[0].shape))

        super().replay()

    # def add_data(self, **kwargs) -> None:
    #
    #     super().add_data(**kwargs)
    #
    #     alpha_pos = kwargs.get('alpha_pos')
    #     beta_pos = kwargs.get('beta_pos')
    #     delta_pos = kwargs.get('delta_pos')
    #     if alpha_pos is not None:
    #     # Handle alpha beta delta
    #
    #         self.__alpha_wolf.append(np.array([np.array(alpha_pos[0]), np.array(alpha_pos[1])]))
    #         self.__beta_wolf.append(np.array([np.array(beta_pos[0]), np.array(beta_pos[1])]))
    #         self.__delta_wolf.append(np.array([np.array(delta_pos[0]), np.array(delta_pos[1])]))
    #
    # def _init(self):
    #     base_artists = super()._init()
    #     self.__alpha_wolf_artist.set_data([], [])
    #     self.__beta_wolf_artist.set_data([], [])
    #     self.__delta_wolf_artist.set_data([], [])
    #
    #     return [*base_artists, self.__alpha_wolf_artist, self.__beta_wolf_artist, self.__delta_wolf_artist]
    #
    # def _animate(self, i: int, frames: int):
    #
    #     base_artists = super()._animate(i, frames)
    #
    #
    #     try:
    #         x_pos, y_pos = self.__alpha_wolf[self._index]
    #         self.__alpha_wolf_artist.set_data(x_pos, y_pos)
    #         self.__alpha_wolf_artist.set_markersize(self._marker_size)
    #
    #         x_pos, y_pos = self.__beta_wolf[self._index]
    #         self.__beta_wolf_artist.set_data(x_pos, y_pos)
    #         self.__beta_wolf_artist.set_markersize(self._marker_size)
    #
    #         x_pos, y_pos = self.__delta_wolf[self._index]
    #         self.__delta_wolf_artist.set_data(x_pos, y_pos)
    #         self.__delta_wolf_artist.set_markersize(self._marker_size)
    #     except:
    #         pass
    #
    #
    #     return [*base_artists, self.__alpha_wolf_artist, self.__beta_wolf_artist, self.__delta_wolf_artist]