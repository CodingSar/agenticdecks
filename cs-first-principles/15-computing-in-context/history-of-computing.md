# History of Computing

> **Layer:** [15 Computing in Context](README.md)
> **Builds on:** [Turing machines](../02-theory-of-computation/03-computability/turing-machines.md), [The MOSFET](../00-engineering-foundations/03-semiconductor-devices/the-mosfet.md), [Fabrication and scaling](../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md), [Packet switching](../08-networking/01-principles/packet-switching.md)
> **Enables:** [Ethics and professional responsibility](ethics-and-professional-responsibility.md), [Law, privacy and policy](law-privacy-and-policy.md)

## Essence

The history of computing is the story of two roots, one formal and one physical, joining and then being scaled up by many orders of magnitude. Logicians in the 1930s defined what computation is; engineers in the 1940s built electronic machines that could hold a program in memory; the transistor and the integrated circuit then made those machines exponentially cheaper for about fifty years. Each drop in cost created a new kind of computing (mainframes, minicomputers, personal computers, networked and mobile devices, cloud and machine learning), and each new kind created new software, new industries and new social questions. Knowing the pressures behind each choice shows which features of today's stack are fundamental and which are accidents.

## Core tenets

1. **The idea of a general-purpose machine predates electronics.** Charles Babbage designed the mechanical Analytical Engine in the 1830s, with a store, a mill and punched-card programs, and Ada Lovelace's 1843 notes on it describe a program and argue the machine could manipulate symbols, not only numbers. It was never built, for lack of funding and precision manufacturing, not of ideas.
2. **Computation was defined before computers existed.** Responding to Hilbert's decision problem, Alonzo Church ([lambda calculus](../02-theory-of-computation/03-computability/lambda-calculus.md)) and Alan Turing ([Turing machines](../02-theory-of-computation/03-computability/turing-machines.md)) gave equivalent definitions of effective computation in 1936, and both showed some problems are [undecidable](../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). Turing's universal machine, one machine that runs any other given its description, is the theoretical stored-program computer. Claude Shannon's 1937 master's thesis showed that relay circuits implement [Boolean algebra](../01-mathematical-foundations/04-algebra/boolean-algebra.md), joining logic to hardware.
3. **War funded the first electronic computers.** Colossus (1943–44) broke German teleprinter ciphers at Bletchley Park; the Electronic Numerical Integrator and Computer (ENIAC, completed 1945) computed artillery tables in the United States; Konrad Zuse's relay-based Z3 (1941) ran in Germany. These machines were programmed by rewiring or by external tape. The 1945 *First Draft of a Report on the EDVAC* (Electronic Discrete Variable Automatic Computer), written by John von Neumann from the EDVAC team's work, described keeping instructions in the same memory as data. The Manchester Baby ran the first stored program in June 1948, and Cambridge's Electronic Delay Storage Automatic Calculator (EDSAC, 1949) offered a regular computing service.
4. **The transistor and integrated circuit made computing cheap.** The transistor (Bell Labs, 1947) replaced unreliable vacuum tubes; the integrated circuit (Kilby and Noyce, 1958–59) put many on one chip. Gordon Moore observed in 1965 that the number of components per chip was doubling at a regular rate (revised in 1975 to about every two years). With Dennard scaling, each generation was also faster and more power-efficient, until about 2005, when power density forced the shift to [multicore](../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md).
5. **Software grew from an afterthought to the dominant cost.** FORTRAN (FORmula TRANslation; Backus's team at International Business Machines (IBM), 1957) showed compiled high-level code could be efficient; LISP (LISt Processor; McCarthy, 1958) and COBOL (COmmon Business-Oriented Language, 1959) followed. By the late 1960s large projects such as IBM's Operating System/360 (OS/360) were late and unreliable; the 1968 North Atlantic Treaty Organization (NATO) conference at Garmisch named this the "software crisis" and coined "software engineering" as a goal.
6. **Time-sharing, Unix and the Internet set the architecture we still use.** Time-sharing (the Compatible Time-Sharing System (CTSS), 1961; Multics) made computers interactive and introduced the problems of [protection](../07-operating-systems/01-kernel-and-abstractions/the-role-of-the-os.md) between users. Unix (Thompson and Ritchie, from 1969) and C (1972) gave a small, portable operating-system model. The Advanced Research Projects Agency Network (ARPANET, 1969), funded by the United States (US) Department of Defense, used [packet switching](../08-networking/01-principles/packet-switching.md); Cerf and Kahn's 1974 internetworking design, later split into the Transmission Control Protocol and Internet Protocol (TCP/IP), connected networks and replaced ARPANET's own protocol on 1 January 1983. Its [end-to-end](../08-networking/01-principles/layering-and-the-end-to-end-principle.md) design kept the network simple and innovation at the edges.
7. **Each cost drop moved computing closer to individuals.** The microprocessor (Intel 4004, 1971) enabled personal computers (Apple II 1977, IBM Personal Computer (PC) 1981). Tim Berners-Lee's World Wide Web (1989–91) made the Internet a public medium. Smartphones (from 2007) put a networked computer in most people's pockets, while cloud computing concentrated servers in a few providers.
8. **Artificial Intelligence (AI) advanced in waves, driven by data and hardware.** The 1956 Dartmouth workshop named "artificial intelligence". Symbolic methods and expert systems rose and fell, with funding collapses ("AI winters") in the 1970s and late 1980s. Neural networks returned when large datasets and [Graphics Processing Units (GPUs)](../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) met: AlexNet (2012) won the ImageNet challenge by a wide margin, and the transformer (2017) led to [large language models](../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md).

## Key concepts

| Term | Meaning |
|---|---|
| Stored-program computer | A machine that holds its instructions in the same memory as data, so programs can be loaded and manipulated like data |
| Von Neumann architecture | The stored-program design described in the 1945 EDVAC report: processor, memory, input and output |
| Moore's law | The observation that transistor counts per chip doubled roughly every two years, for about five decades |
| Dennard scaling | The rule that shrinking transistors kept power density constant; it broke down around 2005 |
| Software crisis | The late-1960s recognition that large software projects were routinely late, over budget and unreliable |
| AI winter | A period of reduced funding and interest after AI expectations went unmet |

## How it fits

- **Below:** history is the narrative of the whole stack: [semiconductor scaling](../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md), [computability](../02-theory-of-computation/03-computability/church-turing-thesis.md), [architecture](../04-computer-architecture/README.md), [languages](../06-programming-languages/README.md), [networks](../08-networking/README.md) and [AI](../13-artificial-intelligence/README.md).
- **Above:** it supplies the cases and context for [ethics](ethics-and-professional-responsibility.md) and shows how [law and policy](law-privacy-and-policy.md) repeatedly lagged new technology.
- **Siblings:** history explains how power over computing became concentrated; ethics and law ask what follows from that power.

## Common misconceptions

- **"Computers were invented by one person."** Stored-program computing came from many groups (Turing, the ENIAC/EDVAC team, Manchester, Cambridge); credit for the "von Neumann" name is still disputed.
- **"Progress was steady and inevitable."** It depended on war funding, a few firms, government research agencies, and physical scaling that has now slowed. Some paths, such as analogue computing, were abandoned for reasons other than merit.
- **"Neural networks are a recent idea."** The perceptron dates from 1958 and backpropagation was popularised in 1986; what was new in the 2010s was data and compute at scale.

## Go deeper

- Paul E. Ceruzzi, *A History of Modern Computing* (2nd ed., 2003): the standard narrative from ENIAC to the Web.
- Martin Campbell-Kelly, William Aspray, Nathan Ensmenger and Jeffrey Yost, *Computer: A History of the Information Machine* (3rd ed., 2014): computing as an economic and social history.
- Alan M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem" (1936): the founding paper of the formal root.
