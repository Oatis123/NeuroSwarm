from rich.progress import Progress, SpinnerColumn, TextColumn
import time


def show_loading_animation():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        
        progress.add_task(description="Restarting application...", total=None)
        
        time.sleep(5)