# testing_azure.github.io

1.	What is CAN and its uses?
2.	CAN frame works?
3.	Why CAN is having 120 ohm at each end?
4.	Why CAN is message oriented protocol?
5.	CAN logic what is follows?
6.	What is CAN arbitration?
7.	How CAN will follow the arbitration?
8.	What is the speed of CAN?
9.	If master send 764 and slaver send 744 which will get the arbitration?
10.	Standard CAN and extended CAN difference?
11.	What is the bit stuffing
12.	What is the use of bit stuffing
13.	What are the functions of CAN transceiver
14.	Functionality of Data link layer layer in CAN 
15.	What is meant by synchronization
16.	What is meant by Hard synchronization and soft synchronization
17.	What is difference between function and physical addressing
18.	What happens if I have to send more than 8 bytes of data
19.	What is kwp2000
20.	What is obdII 
21.	Why diagnostic standards
22.	What is meant by verification and validation
23.	CAN you have 2 transmitters using the same exact header field?
24.	CAN physical layer voltage levels
25.	CAN bit timing
26.	Formula for Baurate calculation
27.	What happen when 2 CAN nodes are sending same identifier at a same time
28.	What is the difference between bit rate and baud rate
29.	What is difference between declaration and definition
30.	What are the different storage classes in C 
31.	What is interrupt
32.	What is software interrupt
33.	What is interrupt latency? How do you measure interrupt lantency ? how to reduce the interrupt latency
34.	Vonneuman and Harvard architecture differences
35.	Risc and cisc differences
36.	What is the booting steps for a cpu
37.	What little endian and big endian, how can I determine whether a machines byte order is big endian or little endian? How can we convert from one to another
38.	Write a program to find unique numbers In a array
39.	Write a program for deletion and insertion of a node in single linked list
40.	Can a variable both const and volatile
41.	What is constant and volatile qualifier
42.	What is the difference between a union and a structure in C
43.	What is meant by structure padding
44.	What is difference between macro and constant in C
45.	What is difference between re-entrant function and recursive function in C
46.	What is the V model ? what is the benefit
47.	What is the black box testing and white box testing
48.	What are the types of testings
49.	The difference between flash and EEPROM, EPROM
50.	Can structures be passed to the functions by value ?
51.	Why cannot arrays be passed by value to function
52.	What is meant by static function
53.	Difference between declaration definition and initialization
54.	What is the difference between pass by value and reference in c 
55.	What is difference between volatile and non volatile memory
56.	What is a reentrant function
57.	Why we are using UDS if CAN support diagnostic communication
58.	How to recover from CAN – busoff
59.	What is virtual functional bus
60.	Intra and inter ECU communication
61.	What is the difference between global and static global variables
62.	How to access a global variables in other files
63.	Why global variable are evil
64.	Why is the use of complex drivers in autosar
65.	How to set clear toggle and checking a single bit in c
66.	What is watchdog timer 
The esensial component in iso26226
67.	What is the difference between 8 bit 16bit and 32 bit processor
68.	What is a function pointer
A function pointer is a variable that strores the address of a function that can later be called through that function pointer
Every time you need a particular behavior such as drawing a line, instead of writing out a bunch of code, all you need to do is call the function, but sometimes you would like to choose different behavior at different time in the same piece of code
69.	Size of datatypes
70.	What is the difference between typedef & macro
Typedef is used to create a new name to an already existing data type, redefine the name create confict with the previous declaration
Macro is a direct substitution of the text before compiling the whole code, in the given example, its just a textual substitution 
71.	What is the difference between a macro and a function
The source code is ready for compilation
Function is calling routine, whence a large programing is dvided into separate portion each portion doing a separate job 
72.	What is inline function, advantage and disavantages

73.	What is difference between a macro and a inline function
Macro
Input argument datatype checking cant be done
Compiler has no idea about macros
Code is not readable
Macro are always expanded or replaced during preprocessing , hence code size is more
Macro cant return
Input 
Input argument datatype can be done
Compiler know about inline function
Code is readable
Inline functions are may not be expanded always
Can return
74.	Preprocessor statement #ifdef, #else, #endif
This provide a rapid way to clip out and insert code

75.	How to calculate CRC sequence in a CAN frame
76.	Difference between static and dynamic RAM
77.	What is difference the between IG and G block in CANalyzer / CANone tool
Thre are 2 limitation to generator block that limit its effectiveness in complex task, the block is misleading for some people because it required multi windown for setting up the transmit message list, the second problem is the block setting have to set before canaluzer measurement start, no changes can be made if the measurement is running
Fortunately , canalyzder has another transmission block that eliminate both practical limitation, the ig combine configuaretion into one window, therefore everything can be setup in one spot
In addition, changes can be made with IG
Without CAPL can we simulate the other ECU can message except test in the CAN simulation network in CANnoe tool without using Ig or G block

78.	What is HIL and SIL testing
Hil – hardware in loop simulation is a technique that is used in development and test of complex real time embedded system , hil simulation provided an effective platform by adding complexity of plant under control to test platform, the complexity of the plant under control is included in test and development by adding a methematical representation of all rlated dynamic system, these mathematical representation are referred to as the plant simulation, the embedded system to be tested interact with this plant simulation
Hil is an effective platform for developing and testing complex real-time embedded system, hil system provide the complexity of the plant under control using methemttiacal representation called plant simulation, of all related dynamic system, it also included electrical emulation of sensof and actualator which act as the interface between the plant simulation and the embedded system under test
Adavatage of hil system
Provides cost saving by shortened development time
Complete consisten test converage
Support automated testing
Enable testing the hardware without building plant prototype
Simulator perform test outside the normal range of operation
Support reproducible test run that assist in uncoreing and tracking down hard to find problem
Enable testing with less risk of destroing the system
SIL refer to kind of testing doen to validate the behavior of the c-code used in the controller
The code can be auto generated from the model used algorithm development
Plant model developd in vehicle simulation environment is importuned to Simulink as a library
Controller is tested in loop with the plant for different routes and speed profiles
Controller is tested for different fault modes of the system using GUI visual connex

79.	What is RTOS
Rtos is a multi tasking os intended for real-time application, it is used on every device/system needing real time operation that means operations based on only on correctness but also upton the time clock cycle in which they are performed
In general, an os is responsible for managing the hardware resources of a computer and hosting application that run on the computer, an rtos perform these task but is also specially designed to run app with very precise timing and a high degree of reliability, this can be especially important in measurement and automation system where downtime is costly or a program delay could cause a safety hazard, to be considedered real-time an os must have known maximum time for each of the critical operation that is perform or at least be able to guarantee that maximum most of the time, some of these operation include os call and interrupt handing, os that can absolutely guarantee a maximum time for these operations are commonly referred to as hard real time while os that can only guarantee a maximum most of time are referred to soft real time
Example : imagein that you are designing an airbag system for a new model of car, in this case , a small error in timing (causing the airbag to deploy too early or too late) , could be catastrophic and cause injiry, therefore a hard real time Is needed, you need assurance as a system designer that no single operation will exceed certain timing constraints , on the other hand, if you were to design a mobile phone that received streaming video it may be ok to lose a small amount of data even though on average it is important to keep up with the video stream, for  this app, a soft real time os may suffice, an rtos can guarantee that a program will run with very consistent timing, real time os do this by providing programmer with a high degree of control over how tasks are priorilize and typically also allow checking to make sure that important deaflines are met
80.	How real time os differ from general purpose os
Os such as Microsoft window and Mac os can provide an excellent platform for developing and running your non critical measurement and control app, however, these os are designed for difference user case than real time os and are not the ideal platform for running app that require precise timing or extended up-time, this section will identify some of the major under the hood …
81.	Interrup latency
IL is measured as the amount of time between when a device generate an interrupt and when that device is servced , while general purpose os may take a variable amount of time to respond to given interrupt , realtime os must guarantee that all interrupt will be services within the certain maximum amount of time in other word the interrup latency of real-time os must be bounded
82.	SPI and I2C difference 
83.	What is UDS advantages
84.	What is cross compiler
85.	Unit/integration/all testing
86.	Regression testing
87.	Testcase type
88.	Malloc calloc
89.	Function pointer advantage where it is used

