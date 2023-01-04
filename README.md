# Sidekick-S-api


## Classes
```mermaid
classDiagram
    class Block
        Block: +int id
        Block: +LABEL obj_type
        Block: +float x_min
        Block: +float x_max
        Block: +float y_min
        Block: +float x_max
        Block: +float confidence
        Block: +List~Text~ Texts
        Block: +List~int~ Next_Blocks
        Block: +List~int~ Previous_Blocks
        Block: +Dict~int,str~ Next_Blocks_Conditionals
        Block: +sort_text()
        Block: +to_string() str
      
    class Text
        Text: +int id
        Text: +float x_min
        Text: +float x_max
        Text: +float y_min
        Text: +float x_max
        Text: +float confidence
        Text: +str text
        Text: +to_string() str
    
    class Pseudocode
        Pseudocode: +List~str~ lines
        Pseudocode: +Dict~any, any~ variables
        Pseudocode: +List~any~ functions
        Pseudocode: +to_pseudocode() str
        Pseudocode: +to_antlr4_pseudocode() str
        Pseudocode: +to_string() str

```

## General flowchart
```mermaid
graph LR
    S1 --> S2
    S2 --> S3
    S3 --> J

    S1[User Input]
    S2[Block Recognition]
    S3[Code Parsing]
    J[Save font code file]
```

## Blocks flowcharts
```mermaid
graph LR
  subgraph SUB3[Code Parsing]
    direction LR
      G --> H
      H --> I
  end
  
  subgraph SUB2[Block Recognition]
    direction LR
      D --> E
      E --> F
  end
  
  subgraph SUB1[User Input]
    direction LR
      A --> B
      B --> C
  end
  
  A[Choose image]
  B[Choose detection system]
  C[Choose output language]
  D[Detect figures]
  E[OCR]
  F[Sort blocks]
  G[Blocks to pseudocode]
  H[ANTRL4 parsing]
  I[ANTLR4 concrete tree to language]
```

## Operations in Process box
- Print:
  - Write any variable without anything
- Scan:
  - Write the variable where to save the data
- Process:
  - Write any math operation (+, -, *, /, /=, *=, +=, -=) between numbers and/or variables
- Decision:
  - It's mandatory draw almost 2 options
  - Inside must be the clause
    - Examples:
      - If statement
        - Box clause: 
          - A <= 1
          - B == 1
          - A != 2
          - ...
        - Options
          - option 1: True
          - option 2: False
      - Switch statement:
        - Box clause: (You must set the variable)
          - VAR
        - Options
          - option 1: 5
          - option 2: 1
          - option 3: 10
          - option default: DEFAULT
    

## Limitations
- Maintain a good separation between arrows in arrow chains
- Letters in only one line
- Conditionals must stay in the nearest arrow to Decision block
- Conditionals statements must finalize on the same block
- Not nest conditionals
- Strings not supported

## TODO-List
- Improve double pointer detection in arrow chains to avoid double detection in the same arrow
  - FlowchartObjectDetection._sort_arrows()
- Improve OCR detection
- String usage
- Functions support
- While loop support
- Do-While loop support
- For loop support
- Switch-case support

## Examples
### Test 1 (TestIf)
![Object list](https://raw.githubusercontent.com/alochimpasplum/Sidekick-S-TFG/Entregable_TFG/TestStuff/TestIf.jpg)
**Abstract syntax tree**
![Object list](https://raw.githubusercontent.com/alochimpasplum/Sidekick-S-TFG/Entregable_TFG/TestStuff/parseTreeIf.png)
**Python**
```
def main():
	VAR1: int = None
	VAR2: int = None
	VAR1 = 2
	VAR2 = input()
	VAR1 *= VAR2
	if VAR1 <= 10:
		VAR1 = 15 * VAR2
	else:
		VAR1 -= VAR2
		VAR1 = VAR1 + 5
		VAR2 = 10 / 5
	VAR1 = VAR1 + VAR2
	print(VAR1)
```
**Java**
```
import java.util.Scanner;

public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int VAR1 = null;
	int VAR2 = null;
	VAR1 = 2;
	VAR2 = scan.nextInt();
	VAR1 *= VAR2;
	if (VAR1 <= 10) {
		VAR1 = 15 * VAR2;
	} else {
		VAR1 -= VAR2;
		VAR1 = VAR1 + 5;
		VAR2 = 10 / 5;
	}
	VAR1 = VAR1 + VAR2;
	System.out.println(VAR1);
}
```

### Test 2 (TestSwitch)
![Object list](https://raw.githubusercontent.com/alochimpasplum/Sidekick-S-TFG/Entregable_TFG/User%20Files/Input%20Images/TestSwitch.jpg)
**Abstract syntax tree**
![Object list](https://raw.githubusercontent.com/alochimpasplum/Sidekick-S-TFG/Entregable_TFG/TestStuff/parseTreeSwitch.png)
**Python**
```
def main():
	VAR: int = None
	VAR = input()
	if VAR == 1:
		VAR -= 1
	elif VAR == 4:
		VAR += 7
		VAR /= 2
	else:
		VAR *= 10
	print(VAR)
```
**Java**
```
import java.util.Scanner;

public static void main(String[] args) {
	Scanner scan = new Scanner(System.in);
	int VAR = null;
	VAR = scan.nextInt();
	switch (VAR) {
		case 1:
			VAR -= 1;
			break;
		case 4:
			VAR += 7;
			VAR /= 2;
			break;
		default:
			VAR *= 10;
	}
	System.out.println(VAR);
}
```


## Objects detected by model
![Object list](https://raw.githubusercontent.com/dbetm/handwritten-flowchart-with-cnn/master/model/set_shapes.png)
#### Original dataset
- Author: ISC UPIIZ students
- Title: Flowchart 3b
- Version: 3.0
- Date: May 2020.
- Editors: Onder F. Campos and David Betancourt.
- Publisher Location: Zacatecas, Mexico.
- Electronic Retrieval Location: https://www.kaggle.com/davbetm/flowchart-3b

#### Used dataset (added pointer detection)
- Electronic Retrieval Location: https://app.roboflow.com/yolo-umkl5/flowchart-etfvh/1