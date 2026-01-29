'''
Docstring for project3.todolist

Project 3: To-Do List (CLI)

Task class with attributes: 
    id (auto increment, primary key), description, priority (low = 2, high = 1), status(pending/done)
    cd 
    #sql to create table if not exists
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        priority INTEGER NOT NULL,
        status TEXT NOT NULL
    );

Milestones
    Add tasks
    View tasks (pending only)
    mark tasks as done
    Delete tasks

Stretch Goals
    Save to file
    Mark tasks as done
    Sort by priority

You’ll Learn
    Lists
    Classes
    CRUD to sqlite
'''
from asyncio import tasks
import sqlite3
from typing import List

database = 'project3/todolist.db'

class Task:
    _task_id: int
    def __init__(self, description: str, priority: int, status: str = 'pending'):
        
        self.description = description
        self.priority = priority
        self.status = status

    @classmethod
    def create(cls,task_id: int, description: str, priority: int, status: str):
        task = cls(description, priority, status)
        task._task_id = task_id
        return task
    
    def __repr__(self):
        return f"|{self._task_id} | {self.description}         |{self.priority}         | {self.status}"
    
def get_db_connection():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

def add_task(description: str, priority: int) -> None:  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, priority, status) VALUES (?, ?, ?)", 
                   (description, priority, 'pending'))
    conn.commit()
    conn.close()

def view_pending_tasks() -> List[Task]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE status = 'pending' ORDER BY priority ASC")
    rows = cursor.fetchall()
    tasks = [Task.create(row['id'], row['description'], row['priority'], row['status']) for row in rows]
    conn.close()
    return tasks

def mark_task_as_done(task_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id: int) -> None:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            priority = int(input("Enter task priority (1 for high, 2 for low): ").strip())
            add_task(description, priority)
            print("Task added successfully.")
        
        elif choice == '2':
            tasks = view_pending_tasks()
            if not tasks:
                print("No pending tasks.")
            else:
                print("-" * 50)
                print(f"{'id':<4}| {'Description':<20}| {'Priority':<9}| {'Status'}")
                print("-" * 50)

                for task in tasks:
                    print(f"{task._task_id:<4}| {task.description:<20}| {task.priority:<9}| {task.status}")
                   
              
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as done: ").strip())
            mark_task_as_done(task_id)
            print("Task marked as done.")
        
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ").strip())
            delete_task(task_id)
            print("Task deleted.")
        
        elif choice == '5':
            print("Exiting To-Do List.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()