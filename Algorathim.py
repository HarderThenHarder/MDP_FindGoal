

class GridWorld:
    score = 50
    state = [0, 1, 2, 3, 4, 5, 6, 7]
    action_space = ['n', 'e', 's', 'w']
    reward = {'0_s': -score,
              '2_s': score,
              '4_s': -score,
              '5_e': -score,
              '5_s': -score,
              '5_w': -score,
              '6_e': score,
              '6_s': score,
              '6_w': score,
              '7_e': -score,
              '7_s': -score,
              '7_w': -score}
    t = {'0_e': 1,
         '0_s': 5,
         '1_w': 0,
         '1_e': 2,
         '2_w': 1,
         '2_s': 6,
         '2_e': 3,
         '3_w': 2,
         '3_e': 4,
         '4_w': 3,
         '4_s': 7,
         '5_n': 0,
         '6_n': 2,
         '7_n': 4}
    v_states = [0, 0, 0, 0, 0, 0, 0, 0]
    gama = 1
    pi_star = []

    def calculate_v(self):
        tmp_v_states = self.v_states

        for i in range(len(self.v_states)):
            tmp_v = 0
            for action in self.action_space:
                key = '%d_%s' % (self.state[i], action)
                if key in self.reward:
                    if key in self.t:
                        tmp_v += 0.25 * (self.reward[key] + self.gama * self.v_states[self.t[key]])
                    else:
                        tmp_v += 0.25 * (self.reward[key] + self.gama * self.v_states[i])
                else:
                    if key in self.t:
                        tmp_v += 0.25 * (-1 + self.gama * self.v_states[self.t[key]])
                    else:
                        tmp_v += 0.25 * (-1 + self.gama * self.v_states[i])
            tmp_v_states[i] = tmp_v

        self.v_states = tmp_v_states

    def calculate_pi(self):
        max_q_pi = 0
        max_a = 'e'
        tmp_q_pi = 0
        pi_star = []

        for i in range(len(self.state)):
            for action in self.action_space:

                key = '%d_%s' % (self.state[i], action)
                if key in self.reward:
                    if key in self.t:
                        tmp_q_pi += 0.25 * (self.reward[key] + self.gama * self.v_states[self.t[key]])
                    else:
                        tmp_q_pi += 0.25 * (self.reward[key] + self.gama * self.v_states[i])
                else:
                    if key in self.t:
                        tmp_q_pi += 0.25 * (-1 + self.gama * self.v_states[self.t[key]])
                    else:
                        tmp_q_pi += 0.25 * (-1 + self.gama * self.v_states[i])

                if tmp_q_pi > max_q_pi:
                    max_q_pi = tmp_q_pi
                    max_a = action

            max_q_pi = 0
            pi_star.append(max_a)

        self.pi_star = pi_star
