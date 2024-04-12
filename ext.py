
# Execute o EPISÓDIO até que você alcance o objetivo
def run_episode(initial_state,reward_matrix, gamma):
    print("Executando...")
    new_state = take_action(initial_state,reward_matrix,gamma)
    while True:
      if new_state == 5:
        break
      else:
        new_state = take_action(new_state,reward_matrix,gamma)

# Execute Diversos EPISÓDIOS até que você alcance o objetivo

def train(episodes, reward_matrix, gamma):
    print("Treinando...")
    for episode in range(episodes):
      print("Episodio Inicial: ",episode)

      #Definindo estado atual
      initial_state = set_initial_state()
      print("Estado Inicial: ",initial_state)

      if initial_state != 5:
        run_episode(initial_state,reward_matrix,gamma)

      print("Episodio final: ",episode)
    print("Treinamento completo!!!")
    return q_matrix


gamma = 0.8
#obtendo a tabela Q
q_table = train(20,rewards,gamma)
print("Tabela Q Final: \n",q_table)

