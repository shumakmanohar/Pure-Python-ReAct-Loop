from rich.console import Console
from rich.rule import Rule

console = Console()


def show_goal(goal: str):
    console.print()
    console.print(Rule("[bold cyan]Goal"))
    console.print(goal)


def show_iteration(iteration: int):
    console.print()
    console.print(Rule(f"[bold yellow]Iteration {iteration}"))


def show_thought(thought: str):
    console.print("[bold cyan]💭 Thought[/bold cyan]")
    console.print(thought)


def show_action(action: str, action_input: str):
    console.print()
    console.print("[bold green]🔧 Action[/bold green]")
    console.print(action)
    console.print(action_input)


def show_observation(observation: str):
    console.print()
    console.print("[bold magenta]👀 Observation[/bold magenta]")
    console.print(observation)


def show_final(answer: str):
    console.print()
    console.print(Rule("[bold green]Final Answer"))
    console.print(answer)
