
                IT5016
 Assessment 3: Programming Principles and Concepts 
                 Name: SURYA PARTAP
         Student ID: 20250248










Link of GITHUB:
https://github.com/ranasuryapartap14/IT4016_assignment3_20250248_suryapartap.git


        Content of Readme
Overview
Programming Principles and Concepts Assessment 3 work, which I created in Programming Principles and Concepts, can be found in this repository.  This project will demonstrate how the ideas of programming can be applied in practice by developing a simple and yet a complete Python application.

The software simulates a staff requisition system to gather staffing information, add items to the requisition, calculate the total cost and make a decision to approve the request.  The program becomes, therefore, easy to maintain, extend, and copy due to the modularity of every element of the program, which can be regarded as a separate functionality. 

Developing a module driven code in more and more advanced steps will indicate that I not only understand the theory behind the concepts, but also the skills that are necessary to get the jobs done. 






Description of the Program
The process operates through four principal stages:
Staff Information (Staff_Info)
•	gathers employee's name, id and date.
•	employs a counter to generate unique requisition id.
Requisitions Total (Requisitions_Total)
•	Imports staff information.
•	allows a user to enter the prices of desired items.
•	The general magnitude of the request is determined by.
Requisition Approval (Requisition_Approval)
•	uses business rule: if the amount is under $500, authorization can be granted automatically.
•	uses staff ID and requisition ID to create an approval reference number.
Display Requisitions (Display_Requisitions)
•	Add everything that's come before.
•	displays reference number, item totals, approval status and staff information and request ID in a report format.




Programming Principles Applied
Each function is responsible for a single role
•	Staff_Info, Requisitions_Total
•	Requisition_Approval
•	Display_Requisitions
 modular design, the code can be much extended and I have applied such important software design principles as KISS, DRY and Separation of Concerns (SoC) in your requisition application.
The code is divided into small and simple functions such as Staff, Info, Requisitions, Total, Requisition, Approval, Display, Requisitions, etc., which have one and one apparent task to perform, and do not require unnecessary complexity, following the KISS principle (Keep It Simple, Stupid). This renders the program simple to follow and support.

The DRY concept (Don't Repeat Yourself) is not merely implemented, but also followed as the information about the staff is collected in one Staff_Info() method and is reused in later methods instead of being typed or requested a number of times.   Also, the program demonstrates the Separation of Concerns (SoC) principle by splitting the logic into a few functions: Staff_Info() is input collection, Requisitions_Total() is required to perform calculations, Requisition_Approval() is the business logic and decision-making, and Display_Requisitions is the final output.  By implementing these ideas, the code will be more organized, easy to handle and easy to modify in future.
Handling Errors
At this point, the program presupposes that the input is real (such as the prices are always numbers).
 Instead, try-except blocks would be used in order to process exceptions and ensure input validation.
Conclusion
There were other parts that I also noted I needed to improve on, which included improved input validation and more complex approval logic.  The next version of the system would involve OOP logic to improve the organised and scaled system.  I would have as an example two classes; Requisition and Staff.
Adding it all up, this repository demonstrates not only that I know code but I can bring out knowledge of the software principles critically and apply them to their practical use.


                     
