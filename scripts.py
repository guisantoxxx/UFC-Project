import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random

def plot_distribution(data, column, bins=30):
    """
    Plota a distribuição de uma coluna numérica usando um histograma e um gráfico de densidade.
    
    Parâmetros:
    - data: DataFrame do pandas contendo os dados
    - column: Nome da coluna numérica a ser plotada
    - bins: Número de bins (intervalos) no histograma (padrão: 30)
    """
    plt.figure(figsize=(5, 3))
    sns.histplot(data[column], bins=bins, kde=True, color='blue', edgecolor='black')
    
    plt.xlabel(column)
    plt.ylabel('Frequência')
    plt.title(f'Distribuição de {column}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

# Exemplo de uso
# plot_distribution(data, 'RedOdds')



from matplotlib.colors import CSS4_COLORS  #

def plot_elo_over_time(fighter_names: list, df: pd.DataFrame):
    """
    Plota o Elo de vários lutadores ao longo do tempo em um único gráfico.
    
    Parâmetros:
        fighter_names (list): Lista de nomes dos lutadores.
        df (pd.DataFrame): DataFrame com as colunas Date, RedFighter, BlueFighter, RedEloCurrent, BlueEloCurrent.
    """
    plt.figure(figsize=(12, 6))
    
    for fighter_name in fighter_names:
        # Filtrar todas as lutas do lutador (como Red ou Blue)
        mask = (df['RedFighter'] == fighter_name) | (df['BlueFighter'] == fighter_name)
        fighter_fights = df[mask].copy()
        
        if fighter_fights.empty:
            print(f"⚠️ Nenhuma luta encontrada para {fighter_name}.")
            continue
        
        # Extrair datas e Elo após cada luta
        dates = []
        elo_history = []
        
        for idx, row in fighter_fights.iterrows():
            date = row['Date']
            # Capturar o Elo APÓS a luta (current)
            if row['RedFighter'] == fighter_name:
                elo = row['RedEloCurrent']
            else:
                elo = row['BlueEloCurrent']
            dates.append(date)
            elo_history.append(elo)
        
        # Criar DataFrame para ordenação e plotagem
        elo_df = pd.DataFrame({'Date': dates, 'Elo': elo_history})
        elo_df = elo_df.sort_values('Date')  # Garantir ordem cronológica
        
        # Escolher uma cor aleatória
        colors = list(CSS4_COLORS.keys())  # Lista de cores disponíveis
        random_color = random.choice(colors)
        
        # Plotar a curva do lutador
        plt.plot(elo_df['Date'], elo_df['Elo'], marker='o', linestyle='-', markersize=8, label=fighter_name, color=random_color)
    
    # Configurações do gráfico
    plt.title('Evolução do Elo de Vários Lutadores', fontsize=14, fontweight='bold')
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Pontuação Elo', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Legenda fora do gráfico
    plt.tight_layout()
    plt.show()
