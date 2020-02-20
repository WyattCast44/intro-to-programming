class Problem:

    signature = '--a'

    description = 'Display the assignment prompt'

    problem = """
Modify the vending status checker to now also report on the status of the machines overall.  Be sure to click the "vending status checker" link above and save the .json files for use in the assignment.

Our current vending status checker produces an inventory report. For each machine's inventory file it is counting how many of each beverage were stocked last time, how many of that beverage are currently in stock, and how many slots the beverage occupies (i.e., each slot holds 8 beverages). Your goal is to modify the program such that it can also produce a machines' sales report, something like this:

Label           Pct Sold   Sales Total  
REID_1F            52.40% $  230.25
REID_2F            42.02% $  138.25
REID_3F            52.07% $  214.75

This report contains three fields: the label of the vending machine, what percentages of the beverages it was last stocked with are sold, and how many total dollars of sales has this generated.

You will need to create a new dictionary where the keys are the vending machine labels, and the values are a new type of object called a `MachineStatus`. For each instance, the `MachineStatus` class should store:

- the label of a vending machine
- the total amount of beverages the vending machine was previously stocked with
- the total amount of beverages currently in stock in the vending machine
- the total income of the machine from the last time it was stocked until now (note: beverages have different prices, so you cannot simply multiply the change in stock times $1.50 to get the total income)

Three major modifciations to `vending_status_checker.py` are necessary:

- adding the `MachineStatus` class
- adding to the loop for counting beverages additional code for counting and updating a vending machine's `MachineStatus` object values
- enabling a user to choose the machines' sales report, not just the inventory report, and then display the report as shown in the following example

Would you like the (m)achine report or the (i)nventory report? m
Label           Pct Sold   Sales Total  
REID_1F            52.40% $  230.25
REID_2F            42.02% $  138.25
REID_3F            52.07% $  214.75

HINT: Start by making sure you understand how the counting is done for inventory, most importantly how the dictionary is used to go from the name a beverage to its `InventoryItem` object. Then create a new dictionary with vending machine labels as keys that maps to the vending machine's `MachineStatus` object. There should be only one `MachineStatus` object for each vending machine.
    """

    def __init__(self, application):
        self.application = application

    def handle(self):
        self.application.output().line(self.problem)
