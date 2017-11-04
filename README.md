# 分詞系統 (Segment System)
- using simple Trie data structure
- maximum matching

## Dependency Intallation
- Python 3.5
```
# we using virtuel environment
$ virtuelenv -p python3.5 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```

## Example

```python
import segment

# 創建你的字典或是載入先前的字典
dictionary = dictionary.Dictionary()
dictionary.load([optional_path])

# 建立斷詞系統，並且可以搭配不同的字典來使用
segments_agent = segment.SegmentSystem()
segments_agent.use_dictionary(dictionary)

context = '''勞神勞力又勞心勞費的勞什骨子喜歡勞什子嗎？'''
segment_list = segments_agent.segments(context)
print(segment_list)
# result: ['勞神', '勞力', '又', '勞心', '勞費', '的', '勞什骨子', '喜歡', '勞什子', '嗎', '？']
```

## How to use?
1. clone this project
2. cd /src
3. initialize dictionary: `python build_dictionary.py`
4. enjoy it!
```
1. Simple input:
(env)$ python main.py -s '今天天氣好冷，這種天氣就想睡覺。睡眠不足的話，會氣噗噗'
# ['今天', '天氣', '好', '冷', '，', '這', '種', '天氣', '就', '想', '睡覺', '。', '睡眠', '不足', '的', '話', '，', '會', '氣', '噗', '噗']

2. File Input:
(env)$ python main.py -f context.txt
# ['今天', '早上', '在', '操場', '看', '到', '一個', '身形', '疲累', '的', '人', '，', '被', '別人', '稱', '作', '勞什骨子', '。', '到底', '勞什骨子', '是', '什麼', '呢', '？']
```