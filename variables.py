from Stop_WatchLogger.database import load_tasks


one_tenth_of_a_second = 0
seconds = 0
minutes = 0
hours = 0
running = False


task_list = load_tasks()
original_task_order = list(task_list.keys())
formatted_tasks = [f"\n{task}: \n{time}\n" for task, time in task_list.items()]