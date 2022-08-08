# Sidekick-S-api

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
      Block: +List~int~ Previous_Blocks
      Block: +List~int~ Next_Blocks
      Block: +to_string() string
      
    class Text
      Text: +int id
      Text: +float x_min
      Text: +float x_max
      Text: +float y_min
      Text: +float x_max
      Text: +float confidence
      Text: +to_string() string

```

## Limitations
- Maintain a good separation between arrows in arrow chains
- [ ] TODO: add images to show how to draw arrows
- All letters must be lowercase
- Letters in only one line

## TODO-List
- Improve double pointer detection in arrow chains to avoid double detection in the same arrow
  - FlowchartObjectDetection._sort_arrows()