from machine_learning_label.classify.BayesianClassify import BayesianClassify
import json
import os
import random

resource_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')


def init_label_id_dict(path):
    """
    初始化标签id字典数据
    :param path: label.json 文件路径
    :return:
    """
    with open(path, "r", encoding="utf-8") as f:
        label_id_dict = json.load(f)
    return label_id_dict['data']


def predict_type(dialogue_content, complain_content, complain_type):
    """
    问题分类标签，在工单类型中的关键字查找来打上这个标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type:
    :return:
    """
    if '网络质量' in complain_type or '基础通信' in complain_type:
        type_predict_label = '基础通信'
    else:
        type_predict_label = ''
    return type_predict_label


def predict_communication(dialogue_content, complain_content, complain_type_arr):
    """
    基础通信标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type_arr:
    :return:
    """
    communication_predict_label = ''
    for ot in complain_type_arr:
        if '语音基本业务' in ot or '语音通话' in ot or '话音基本业务' in ot:
            communication_predict_label = '语音通话'
            break
        elif '互联网' in ot or '上网' in ot:
            communication_predict_label = '手机上网'
            break
        elif '消息类业务' in ot or '短彩信' in ot:
            communication_predict_label = '短彩信'
            break
        elif 'VoLTE' in ot or 'VOLTE' in ot:
            communication_predict_label = 'VoLTE'
            break
    return communication_predict_label


def predict_network(dialogue_content, complain_content, complain_type_arr):
    """
    网络制式标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type_arr:
    :return:
    """
    network_predict_label = ''
    for ot in complain_type_arr:
        if '2G/3G' in ot or '2、3G' in ot or '2/3G' in ot:
            network_predict_label = '2G'
            break
        elif '4G' in ot:
            network_predict_label = '4G（LTE）'
            break
    return network_predict_label


def predict_device(dialogue_content, complain_content, complain_type_arr):
    """
    设备类型标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type_arr:
    :return:
    """
    device_predict_label = ''
    for ot in complain_type_arr:
        if '手机上网' in ot or '语音' in ot or '通话' in ot or '互联网' in ot or '语音基本业务' in ot:
            device_predict_label = '手机'
            break
        elif 'MIFI' in ot:
            device_predict_label = 'MIFI'
            break
        elif 'CPE' in ot:
            device_predict_label = 'CPE'
            break
    return device_predict_label


def predict_duration(dialogue_content, complain_content, complain_type):
    """
    问题时长标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type:
    :return:
    """
    duration_label = ''
    dialogue_content = dialogue_content.replace('A: ', '').replace('B: ', '').replace('\n', '')
    if '今天' in dialogue_content:
        duration_label = '1天'
    elif '昨天' in dialogue_content or '两天' in dialogue_content or '三天' in dialogue_content:
        duration_label = '2-3天'
    elif '一个星期' in dialogue_content or '两个星期' in dialogue_content:
        duration_label = '7-14天'
    elif '半个月' in dialogue_content:
        duration_label = '15天'
    elif '一个月' in dialogue_content:
        duration_label = '1个月'
    elif '三个月' in dialogue_content:
        duration_label = '3个月'
    elif '半年' in dialogue_content:
        duration_label = '6个月'
    elif '一年' in dialogue_content:
        duration_label = '1年'
    elif '一年以上' in dialogue_content:
        duration_label = '1年以上'
    elif '一直都有' in dialogue_content:
        duration_label = '一直都有'
    return duration_label


def predict_phenomenon(dialogue_content, complain_content, complain_type_arr):
    """
    现象标签
    :param dialogue_content:
    :param complain_content:
    :param complain_type_arr:
    :return:
    """
    phenomenon_predict_label = ''
    for ot in complain_type_arr:
        if '主叫不能接通' in ot:
            phenomenon_predict_label = '主叫不能接通'
            break
        elif '被叫不能接通' in ot:
            phenomenon_predict_label = '被叫不能接通'
            break
        elif '主被叫均不能接通' in ot:
            phenomenon_predict_label = '主被叫均不能接通'
            break
        elif '掉话' in ot:
            phenomenon_predict_label = '用户掉话'
            break
        elif '串线' in ot:
            phenomenon_predict_label = '用户串线'
            break
        elif '单通' in ot:
            phenomenon_predict_label = '用户单通'
            break
        elif '时断时续' in ot:
            phenomenon_predict_label = '通话时断时续'
            break
        elif '回声' in ot or '回音' in ot:
            phenomenon_predict_label = '用户回音'
            break
        elif '噪音' in ot or '杂音' in ot:
            phenomenon_predict_label = '用户背景噪音'
            break
        elif '软件断线' in ot or '信号时好时坏' in ot:
            phenomenon_predict_label = '上网时出现断线'
            break
        elif '网速慢或网页无法打开' in ot:
            phenomenon_predict_label = '网速慢或网页无法打开'
            break
        elif '无法使用' in ot:
            phenomenon_predict_label = '有信号但无法使用'
            break
        elif '无信号' in ot or '网络覆盖' in ot:
            phenomenon_predict_label = '没有信号'
            break
    return phenomenon_predict_label


def predict_place(dialogue_content, complain_content, complain_type):
    """
    场景1,场景2
    :param dialogue_content:
    :param complain_content:
    :param complain_type:
    :return:
    """
    place1_predict_label = ''
    place2_predict_label = ''
    contents = complain_content.split('；')
    for content in contents:
        od = content.split('：')
        if '询问用户故障发生地为室内还是室外' in od[0]:
            place1_predict_label = od[1]
        elif '补充信息' in od[0]:
            if od[1][:2] == '场景':
                place2_predict_label = od[1][3:-1]
    return place1_predict_label, place2_predict_label


def predict_sentiment_titer(dialogue_content, complain_content, complain_type):
    """
    情绪效价
    :param dialogue_content:
    :param complain_content:
    :param complain_type:
    :return:
    """


class Label:

    def __init__(self):
        self.compete_clf = BayesianClassify('words/compete_word.txt', 'train_set/compete_data.xlsx')
        self.behavior_clf = BayesianClassify('words/behavior_word.txt', 'train_set/behavior_data.xlsx')
        self.infinite_clf = BayesianClassify('words/infinite_word.txt', 'train_set/infinite_data.xlsx')
        self.net_service_clf = BayesianClassify('words/net_service_word.txt', 'train_set/net_service_data.xlsx')
        self.label_id_dict = init_label_id_dict(os.path.join(resource_path, 'label.json'))

    def get_label_id(self, p_label, label):
        if label == '':
            return label
        for lb in self.label_id_dict:
            for l in lb['children']:
                if l['tagName'] == p_label:
                    children = l['children']
                    for child in children:
                        if child['tagName'] == label:
                            return str(child['id']) + '#' + label
        return label

    def get_label(self, dialogue_content, complain_content, complain_type):
        """
        打标签
        :param dialogue_content: 对话文本内容
        :param complain_content: 工单投诉内容
        :param complain_type: 投诉类型
        :return:
        """
        complain_type_arr = complain_type.split('->')
        # 问题分类标签
        type_predict_label = predict_type(dialogue_content, complain_content, complain_type)
        # 基础通信标签
        communication_predict_label = predict_communication(dialogue_content, complain_content, complain_type_arr)
        # 网络制式标签
        network_predict_label = predict_network(dialogue_content, complain_content, complain_type_arr)
        # 设备类型标签
        device_predict_label = predict_device(dialogue_content, complain_content, complain_type_arr)
        # 问题时长标签
        duration_label = predict_duration(dialogue_content, complain_content, complain_type)
        # 现象标签
        phenomenon_predict_label = predict_phenomenon(dialogue_content, complain_content, complain_type_arr)
        # 场景1,场景2
        place1_predict_label, place2_predict_label = predict_place(dialogue_content, complain_content,
                                                                   complain_type)

        compete_predict_label = self.compete_clf.predict(dialogue_content)
        behavior_predict_label = self.behavior_clf.predict(dialogue_content)
        infinite_predict_label = self.infinite_clf.predict(dialogue_content)
        net_service_predict_label = self.net_service_clf.predict(dialogue_content)

        concentration = ''
        sentiment_titer_label = '中性'
        sentiment_reason_label = ''

        # 情绪效价
        # sentiment_titer_label = predict_sentiment_titer(dialogue_content, complain_content, complain_type)

        if behavior_predict_label != '' or net_service_predict_label != '':
            concentration = random.randint(30, 60)
            sentiment_titer_label = '负性'

        if behavior_predict_label == '投诉升级':
            concentration = random.randint(95, 99)
        elif behavior_predict_label == '离网倾向':
            concentration = random.randint(90, 95)
        elif behavior_predict_label == '敏感用户':
            concentration = random.randint(80, 90)
        elif behavior_predict_label == '情绪用户':
            concentration = random.randint(70, 80)

        if net_service_predict_label == '无响应':
            sentiment_reason_label = '无反馈'
            concentration = random.randint(60, 70)

        labels = {
            'type': self.get_label_id('分类', type_predict_label),
            'device': self.get_label_id('设备类型', device_predict_label),
            'network': self.get_label_id('网络制式', network_predict_label),
            'communication': self.get_label_id('问题现象', communication_predict_label),
            'place1': self.get_label_id('场景1类', place1_predict_label),
            'place2': self.get_label_id('场景2类', place2_predict_label),
            'phenomenon': self.get_label_id('问题现象', phenomenon_predict_label),
            'behavior': self.get_label_id('用户特征', behavior_predict_label),
            'infinite': self.get_label_id('不限量套餐', infinite_predict_label),
            'analysis': self.get_label_id('竞对覆盖', compete_predict_label),
            'netService': self.get_label_id('网络服务', net_service_predict_label),
            'sentimentConcentration': concentration,
            'sentimentDuration': self.get_label_id('问题时间', duration_label),
            'sentimentTiter': self.get_label_id('情绪效价', sentiment_titer_label),
            'sentimentReason': self.get_label_id('低满意度原因', sentiment_reason_label)
        }
        return labels


if __name__ == '__main__':
    clf = Label()
    # print(clf.get_label_id('场景2类', '农村'))
    print(clf.get_label('A: 对啊，你好很高兴为您服务为您好我，知道，给我老汉儿电电话号码别人打电话打不通打不通诶。B: 是所有号码都打不通对不对。'
                        'A: 诶我现在给你打电话别人打过来给您打过电话就打不通。B: 嗯那个对不起用户添麻烦了，那这边的话我想冒昧问一下，'
                        '呃别人给您打不通的话对方那边有什么提示吗？A: 怎么提示都没有。B: 哎别人打不进来您自己打出去没问题吗？A: 呃我打出去没问'
                        '题啊。B: 可以帮我提供一下您的使用地址吗比如您现在在什么地方使用别人给您代办？A: 上面，烟霞，这上面。B: 嗯然后呢。'
                        'A: 啊涪城区。B: 啊涪城区。A: 哎。B: 呃详细的地址有没有流量现在。A: 现我现在开车多久啊，天气预报是。'
                        'B: 哎您之前的话在什么地方使用别人密码的？A: 流量业务一下数据是多少，我再扣的也扣流量小这边儿，嗯什么乡桥扣你交钱？'
                        '还是否则扣吗？对对对对对，喂这个我原来喂。B: 噢我原来为。A: 嗯，现在扣了就行别在这里，我上次也出现这个问题的上次你们那'
                        '个什么给我说了一个数字然后我打了一下然后就可以了？B: 您说的是那个井井，呃就是那个是今天二幺井嘛你说那个是取消呼叫限制'
                        '这种吗？A: 对对对对好像是这个，嗯但是好像给我说说过然后我打了一次就可以了。B: 噢那稍后您需要的话你也可以打吗？另外我'
                        '通过系统上查了一下上面显示您的那个状态的话网络状态我看的话正常的也没问题。那然后的话我这边的话，就想把那个网络数据就把'
                        '这个情况吗？呃我通过系统的话进行了一下那个登记上报，稍后的话会给您把那个数据呢，进行一下修复处理，就是我想问先生键那'
                        '个能打不能接的话，如果说我们在处理过程中，或者完了过后需要联系有没有其它号码能够正常跟您联系的到有没有我能接人接我只能'
                        '接一个号码但是两个号码我就。A: 就接不了了，哦，我的意思是，以前我现在给你打电话可以然后，北别人给我打的时候就打不进来了'
                        '。B: 那您的意思是说在通话中的时候别人给你打电话吗？A: 对对对对对对就今天别人打不通我电话了。B: 那之前的话能用完。'
                        'A: 之前可以今天早上也就现在不行了。B: 那您这边的话它是一个叫呼叫保持或者是，就呼叫限制呼叫保持这个功能吗？那您稍后的'
                        '话可以检测一下手机上那个功能是不是这个正常打开的呢。A: 有没有不小心打开看，是打开的，打开那个电话我看，您好，诶，就'
                        '你给我说一个什么井井二幺井那个我打一下子我看试一下看行不行吗？B: 呃您要说的话您稍后可以试一下嘛。A: 哎哎哎别人打进'
                        '来我给你打电话的时候别人就打不进来啦，怎么，真的没有然后就挂了。B: 嗯它这个的话就是呼叫保持和呼叫限制的一个功能，也就'
                        '那个活动了呼叫等待的一个功能吗？那您是。A: 需要您。B: 啊。A: 我试一下我试一下我取消。B: 嗯嗯好您可以试一下到时候或'
                        '者说的话如果不行的话也可以换机换卡检测一下嘛好吧。A: 嗯好的好的好的好的。B: 好那还有其他什么问题吗？A: 啊没有啦没有'
                        '啦。B: 好那感谢来电了再见。', '<Guid dataid="19'
                                           '0323181416573"/>询问用户：为准确排查您反映的问题原因，需要通过系统获取您的相关功能状态和网络状态可以吗？是否同意：'
                                           '同意；1、打接电话问题；2、系统判断当前是否向用户播报过IVR群障信息：否；3、系统判断是否漫游：非省际漫游(四川用户在四川)'
                                           '；4、系统判断BOSS状态是否正常：正常；5、Boss系统判断是否VOLTE用户：非VOLTE用户；6、询问客户是属于哪种无法使用：'
                                           '普通语音问题；7、询问用户当前位置是否为故障地址：是；8、询问用户具体故障现象：无法主被叫；9、询问用户具体故障现象：'
                                           '用户无法拨打电话；10、系统自动查询客户主叫功能是否正常：主叫功能正常；11、系统判断用户是否有ENUM(号码映射)或Tas数据：'
                                           '无相关数据；12、询问用户离开故障地是否恢复：恢复；13、询问用户是在与个别用户通话中出现该情况还是与所有用户通话过程中出现'
                                           '该情况：所有或不清楚；14、生成工单；补充信息：场景(其他)；故障时间：2019-03-23 18',
                        '服务类->客户投诉->基础通信->话音基本业务->通话质量->用户无法主被叫->被叫不能接通'))
