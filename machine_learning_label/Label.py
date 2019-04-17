from machine_learning_label.classify.BayesianClassify import BayesianClassify


class Label:

    def __init__(self):
        self.compete_clf = BayesianClassify('words/compete_word.txt', 'train_set/compete_data',
                                            'train_set/label/compete_label.txt')
        self.behavior_clf = BayesianClassify('words/behavior_word.txt', 'train_set/behavior_data',
                                             'train_set/label/behavior_label.txt')
        self.infinite_clf = BayesianClassify('words/infinite_word.txt', 'train_set/infinite_data',
                                             'train_set/label/infinite_label.txt')
        self.net_service_clf = BayesianClassify('words/net_service_word.txt', 'train_set/net_service_data',
                                                'train_set/label/net_service_label.txt')

    def get_label(self, dialogue_content, complain_content, complain_type):
        """
        打标签
        :param dialogue_content: 对话文本内容
        :param complain_content: 工单投诉内容
        :param complain_type: 投诉类型
        :return:
        """
        type_predict_label = ''
        device_predict_label = ''
        network_predict_label = ''
        communication_predict_label = ''
        place_predict_label1 = ''
        place_predict_label2 = ''
        phenomenon_predict_label = ''
        duration_label = ''
        concentration = ''
        feature_label = ''
        sentiment_titer = ''
        sentiment_reason = ''

        compete_predict_label = self.compete_clf.predict(dialogue_content)
        behavior_predict_label = self.behavior_clf.predict(dialogue_content)
        infinite_predict_label = self.infinite_clf.predict(dialogue_content)
        net_service_predict_label = self.net_service_clf.predict(dialogue_content)

        labels = {
            'type': type_predict_label,
            'device': device_predict_label,
            'network': network_predict_label,
            'communication': communication_predict_label,
            'place1': place_predict_label1,
            'place2': place_predict_label2,
            'phenomenon': phenomenon_predict_label,
            'behavior': behavior_predict_label,
            'infinite': infinite_predict_label,
            'analysis': compete_predict_label,
            'netService': net_service_predict_label,
            'sentimentConcentration': concentration,
            'sentimentDuration': duration_label,
            'sentimentTiter': sentiment_titer,
            'sentimentFeature': feature_label,
            'sentimentReason': sentiment_reason
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
