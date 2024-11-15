import tkinter as tk
from tkinter import ttk


def calculate_cost():
    x = athlete_name_entry.get()
    training_plan = training_plan_var.get()
    # Check if the training plan is one of the fixed costs
    if training_plan == 25 or training_plan == 30 or training_plan == 35:
        weight = weight_entry.get()
        i = int(weight)
        weight_category = weight_category_var.get()

        competition_fee = 22 * int(competition_entry.get())
        r = float(competition_fee)
        # Determine the upper weight limit based on the selected weight category
        if weight_category == "Heavyweight over 100kg":
            upper_weight_limit = 101
            y = (upper_weight_limit)
        elif weight_category == "LightHeavyweight":
            upper_weight_limit = 100
            y = (upper_weight_limit)
        elif weight_category == "Middleweight":
            upper_weight_limit = 90
            y = (upper_weight_limit)
        elif weight_category == "LightMiddleweight":
            upper_weight_limit = 81
            y = (upper_weight_limit)
        elif weight_category == "Lightweight":
            upper_weight_limit = 73
            y = (upper_weight_limit)
        elif weight_category == "Flyweight":
            upper_weight_limit = 66
            y = (upper_weight_limit)
        else:
            output_label.config(text="Error")
        # Check if the weight is within the selected category limits

        if i<=65 and y<=66 or i>=66 and i>=y:
            training_cost = (training_plan * 4)
            total_cost = (training_plan * 4) + r
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost £{training_cost}")
            output_label2.config(text=f"Competition fee £{r}")

            output_label3.config(text=f"Monthly Total cost for {x} is £{total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")

            output_label5.config(text="No Error ")



        else:
            training_cost = (training_plan * 4)
            total_cost = (training_plan * 4) + r
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost £{training_cost}")
            output_label2.config(text=f"Competition fee £{r}")

            output_label3.config(text=f"Monthly Total cost for {x} is £{total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")

            output_label5.config(text="suggestion: choose below weight category from your current weight")


            return
    # Check if the training plan is the hourly cost plan
    elif training_plan == 9.50:
        weight = weight_entry.get()
        i = int(weight)
        weight_category = weight_category_var.get()
        # Determine the upper weight limit based on the selected weight category
        if weight_category == "Heavyweight over 100kg":
            upper_weight_limit = 101
            y = (upper_weight_limit)
        elif weight_category == "LightHeavyweight":
            upper_weight_limit = 100
            y = (upper_weight_limit)
        elif weight_category == "Middleweight":
            upper_weight_limit = 90
            y = (upper_weight_limit)
        elif weight_category == "LightMiddleweight":
            upper_weight_limit = 81
            y = (upper_weight_limit)
        elif weight_category == "Lightweight":
            upper_weight_limit = 73
            y = (upper_weight_limit)
        elif weight_category == "Flyweight":
            upper_weight_limit = 66
            y = (upper_weight_limit)
        else:
            output_label.config(text="Error")
        # Check if the weight is within the selected category limits
        if i <= 65 and y <= 66 or i >= 66 and i >= y:

            competition_fee = 22 * int(competition_entry.get())
            hours = (hours_entry.get())

            training_cost = (training_plan * float(hours_entry.get()))
            total_cost = (9.50 * float(hours_entry.get())) + float(competition_fee)
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost ${training_cost}")
            output_label2.config(text=f"Competition fee ${float(competition_fee)}")

            output_label3.config(text=f"Monthly Total cost for {x} is ${total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n_________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")

            output_label5.config(text="No Error ")

        else:
            competition_fee = 22 * int(competition_entry.get())
            hours = (hours_entry.get())

            training_cost = (training_plan * float(hours_entry.get()))
            total_cost = (9.50 * float(hours_entry.get())) + float(competition_fee)
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost ${training_cost}")
            output_label2.config(text=f"Competition fee ${float(competition_fee)}")

            output_label3.config(text=f"Monthly Total cost for {x} is ${total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n_________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")

            output_label5.config(text="suggestion: choose below weight category from your current weight")

            return


    # Check if the training plan is a special fixed cost plan

    elif training_plan == 22:

        weight = weight_entry.get()
        i = int(weight)
        weight_category = weight_category_var.get()

        competition_fee = 22 * int(competition_entry.get())
        r = float(competition_fee)

        if weight_category == "Heavyweight over 100kg":
            upper_weight_limit = 101
            y = (upper_weight_limit)
        elif weight_category == "LightHeavyweight":
            upper_weight_limit = 100
            y = (upper_weight_limit)
        elif weight_category == "Middleweight":
            upper_weight_limit = 90
            y = (upper_weight_limit)
        elif weight_category == "LightMiddleweight":
            upper_weight_limit = 81
            y = (upper_weight_limit)
        elif weight_category == "Lightweight":
            upper_weight_limit = 73
            y = (upper_weight_limit)
        elif weight_category == "Flyweight":
            upper_weight_limit = 66
            y = (upper_weight_limit)
        else:
            output_label.config(text="Error")
        # Check if the weight is within the selected category limits

        if i <= 65 and y <= 66 or i >= 66 and i >= y:
            training_cost = (training_plan * 4)
            total_cost = (training_plan * 4) + r
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost ${training_cost}")
            output_label2.config(text=f"Competition fee ${r}")

            output_label3.config(text=f"Monthly Total cost for {x} is ${total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")
            output_label5.config(text="No Error ")



        else:
            training_cost = (training_plan * 4)
            total_cost = (training_plan * 4) + r
            output_label.config(text=f"Athlete name is {x}")
            output_label1.config(text=f"monthly training cost ${training_cost}")
            output_label2.config(text=f"Competition fee ${r}")

            output_label3.config(text=f"Monthly Total cost for {x} is ${total_cost} ")
            output_label4.config(text=" |Categories               | upper weight limit(kg)"
                                      "\n________________________________________________"
                                      "\n |Heavyweight            =Unlimited(over 100)"
                                      "\n |Light-Heavyweight = 100"
                                      "\n |Middleweight           = 90"
                                      "\n |Light-Middleweight = 81"
                                      "\n |Lightweight               = 73"
                                      "\n |Flyweight                   = 66")

            output_label5.config(text="suggestion: choose below weight category from your current weight")

            return


root = tk.Tk()
root.configure(bg="gray51")
all_font = ("arial", 14, "bold")

root.title("Judo Training Cost cal")
# first label
first_label = ttk.Label(root, text="Welcome to North Sussex Judo", font="all_font", foreground="snow",
                        background="gray51")
first_label.grid(row=0, column=0, columnspan=2, pady=5, )

# Athlete name entry
athlete_name_label = ttk.Label(root, text="Athlete name:", font="all_font", foreground="snow", background="gray51")

athlete_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
athlete_name_entry = ttk.Entry(root)

athlete_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Training plan selection
training_plan_label = ttk.Label(root, text="Training Plan", font="all_font", foreground="snow", background="gray51")
training_plan_label.grid(row=2, column=0, pady=5, padx=5, sticky="e")
training_plan_var = tk.DoubleVar()
training_plan_combobox = ttk.Combobox(root, textvariable=training_plan_var, values=[25, 30, 35, 9.50, 22])
training_plan_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Weight input
weight_label = ttk.Label(root, text="Your Weight(kg):", font="all_font", foreground="snow", background="gray51")
weight_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
weight_entry = ttk.Entry(root)
weight_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")

# weight chart
chart_label = ttk.Label(root, text="YOUR WEIGHT > CHOOSING WEIGHT CATEGORY", font="all_font", foreground="snow",
                        background="gray51")
chart_label.grid(row=4, column=1, pady=5, padx=5, sticky="w")
chart_label1 = ttk.Label(root, foreground="white", background="gray51",
                         text=" |Categories                 | upper weight limit(kg)"
                              "\n------------------------------------------------"
                              "\n |Heavyweight            =Unlimited(over 100)"
                              "\n |Light-Heavyweight = 100"
                              "\n |Middleweight           = 90"
                              "\n |Light-Middleweight = 81"
                              "\n |Lightweight               = 73"
                              "\n |Flyweight                   = 66")

chart_label1.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Weight category select
weight_category_label = ttk.Label(root, text="Weight category:", font="all_font", foreground="snow",
                                  background="gray51")
weight_category_label.grid(row=6, column=0, pady=5, padx=5, sticky="e")
weight_category_var = tk.StringVar()
weight_category_combobox = ttk.Combobox(root, textvariable=weight_category_var,
                                        values=["Heavyweight over 100kg", "LightHeavyweight", "Middleweight",
                                                "LightMiddleweight", "Lightweight", "Flyweight"])
weight_category_combobox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# private tution hours
hours_label = ttk.Label(root, text="hours", font="all_font", foreground="snow", background="gray51")
hours_label.grid(row=7, column=0, pady=5, padx=5, sticky="e")
hours_entry = ttk.Entry(root)
hours_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")
hours_label1 = ttk.Label(root, text="(only for $9.5 training plan)", font="all_font", foreground="snow",
                         background="gray51")
hours_label1.grid(row=7, column=1, padx=5, pady=5)

# Competition entry
competition_label = ttk.Label(root, text="Competitions: ", font="all_font", foreground="snow", background="gray51")
competition_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
competition_entry = ttk.Entry(root)
competition_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

# Calculate button
calculate_button = ttk.Button(root, text="calculate", command=calculate_cost)
calculate_button.grid(row=9, column=0, columnspan=2, pady=7)

# output
output_label = ttk.Label(root, text="", foreground="black", background="gray51")
output_label.grid(row=10, column=0, columnspan=2)
output_label1 = ttk.Label(root, text="", foreground="black", background="gray51")
output_label1.grid(row=11, column=0, columnspan=2)
output_label2 = ttk.Label(root, text="", foreground="black", background="gray51")
output_label2.grid(row=12, columnspan=2, column=0)
output_label3 = ttk.Label(root, text="", foreground="black", background="gray51")
output_label3.grid(row=13, columnspan=2, column=0)
output_label4 = ttk.Label(root, text="", foreground="black", background="gray51")
output_label4.grid(row=14, columnspan=2, column=0)
output_label5 = ttk.Label(root, text="", foreground="black", background="gray51")
output_label5.grid(row=15, columnspan=2, column=0)


root.mainloop()

