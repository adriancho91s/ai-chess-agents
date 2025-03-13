import chess
import chess.svg
from IPython.display import display, SVG, clear_output
import time
import chess.pgn
from agents import RandomAgent
from agents import HillClimbingAgent
from agents import SimulatedAnnealingAgent
from agents import MinimaxAgent
from agents import AlphaBetaAgent
from agents import Heuristics


def choose_display_mode():
    """
    Prompts the user to select the display mode for the chess game.

    Returns:
        bool: True if graphical mode (chess.svg) is selected, False if text mode is selected.
    """
    mode = input("Seleccione el modo de visualización: (1) Gráfico (chess.svg) o (2) Texto: ")
    return True if mode.strip() == "1" else False


visualize_mode = choose_display_mode()


def choose_delay_render_time():
    """
    Prompts the user to input the delay time for rendering frames.

    Returns:
        float: The delay time in seconds.
    """
    return float(input("Escribe el tiempo de retraso para cambiar de frame (en segundos):"))


render_delay = choose_delay_render_time()


def play_game(agent1, agent2, max_moves=400, visualize=True, render_delay=0.5):
    """
    Plays a game between two chess agents.

    Args:
        agent1 (ChessAgent): The first chess agent.
        agent2 (ChessAgent): The second chess agent.
        max_moves (int): The maximum number of moves in the game.
        visualize (bool): Whether to visualize the game.
        render_delay (float): The delay time for rendering frames.

    Returns:
        tuple: The result of the game and the duration of the game.
    """
    board, move_count, start_time = chess.Board(), 0, time.time()
    agents = {True: agent1, False: agent2}
    print(f"Game Start: {agent1.__class__.__name__} vs {agent2.__class__.__name__}")

    while not board.is_game_over() and move_count < max_moves:
        move = agents[board.turn].select_move(board)
        board.push(move)
        move_count += 1
        if visualize:
            clear_output(wait=True)
            display(SVG(chess.svg.board(board, size=400)))
            time.sleep(render_delay)
        else:
            clear_output(wait=True)
            time.sleep(render_delay)
            print("-----------------------")
            print(board)

    print(f"Game Over: {board.result()} - Moves: {move_count}")
    return board.result(), time.time() - start_time


def extract_openings_from_pgn(pgn_file, max_openings=100):
    """
    Extracts opening moves from a PGN file.

    Args:
        pgn_file (str): The path to the PGN file.
        max_openings (int): The maximum number of openings to extract.

    Returns:
        list: A list of opening moves.
    """
    openings = []
    with open(pgn_file) as f:
        while len(openings) < max_openings:
            game = chess.pgn.read_game(f)
            if game is None:
                break
            board = game.board()
            opening_moves = []
            for move in game.mainline_moves():
                opening_moves.append(move.uci())
                board.push(move)
                if len(opening_moves) >= 5:
                    break
            openings.append(opening_moves)
    return openings


try:
    pgn_file = "/mnt/data/Novikov.pgn"
    openings = extract_openings_from_pgn(pgn_file)
    print(f"Se extrajeron {len(openings)} aperturas.")
except Exception as e:
    print(f"Error: {e}")
    openings = []

agents_with_openings = [
    (RandomAgent, None, openings),
    (HillClimbingAgent, (Heuristics.evaluate_material, "Material Evaluation"), openings),
    (HillClimbingAgent, (Heuristics.evaluate_relative_difference, "Relative Difference"), openings),
    (SimulatedAnnealingAgent, (Heuristics.evaluate_material, "Material Evaluation"), openings),
    (SimulatedAnnealingAgent, (Heuristics.evaluate_relative_difference, "Relative Difference"), openings),
    (AlphaBetaAgent, 3, (Heuristics.evaluate_material, "Material Evaluation"), openings),
    (AlphaBetaAgent, 3, (Heuristics.evaluate_relative_difference, "Relative Difference"), openings),
    (MinimaxAgent, 3, (Heuristics.evaluate_material, "Material Evaluation"), openings),
    (MinimaxAgent, 3, (Heuristics.evaluate_relative_difference, "Relative Difference"), openings),
]


def agent_description(agent_tuple):
    """
    Generates a description for an agent tuple.

    Args:
        agent_tuple (tuple): The agent tuple.

    Returns:
        str: The description of the agent.
    """
    if len(agent_tuple) == 3:
        if agent_tuple[1] is None:
            return agent_tuple[0].__name__
        else:
            heuristic_name = agent_tuple[1][1]
            return f"{agent_tuple[0].__name__} (heuristic: {heuristic_name})"
    elif len(agent_tuple) == 4:
        heuristic_name = agent_tuple[2][1]
        return f"{agent_tuple[0].__name__} (depth: {agent_tuple[1]}, heuristic: {heuristic_name})"
    return agent_tuple[0].__name__


stats_with_openings = {agent_description(agent): {"wins": 0, "losses": 0, "draws": 0}
                       for agent in agents_with_openings}

for agent1 in agents_with_openings:
    for agent2 in agents_with_openings:
        if agent1 != agent2:
            if len(agent1) == 3:
                if agent1[1] is None:
                    agent1_instance = agent1[0](True, agent1[2])
                else:
                    agent1_instance = agent1[0](True, agent1[1][0], agent1[2])
            if len(agent2) == 3:
                if agent2[1] is None:
                    agent2_instance = agent2[0](False, agent2[2])
                else:
                    agent2_instance = agent2[0](False, agent2[1][0], agent2[2])

            result, _ = play_game(agent1_instance, agent2_instance, visualize=visualize_mode, render_delay=render_delay)
            desc1 = agent_description(agent1)
            desc2 = agent_description(agent2)
            if result == "1-0":
                stats_with_openings[desc1]["wins"] += 1
                stats_with_openings[desc2]["losses"] += 1
            elif result == "0-1":
                stats_with_openings[desc1]["losses"] += 1
                stats_with_openings[desc2]["wins"] += 1
            else:
                stats_with_openings[desc1]["draws"] += 1
                stats_with_openings[desc2]["draws"] += 1

print("\nFinal Tournament Results (With Openings):")
for agent_desc, record in stats_with_openings.items():
    """
    Prints the final tournament results.

    Args:
        agent_desc (str): The description of the agent.
        record (dict): The record of wins, losses, and draws for the agent.
    """
    print(f"{agent_desc}: Wins: {record['wins']}, Losses: {record['losses']}, Draws: {record['draws']}")