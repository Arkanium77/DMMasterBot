from random import randrange as rnd

rofles=(
    """Проснулись эльфы, и увидели звезды, ибо лежали на спине, и полюбили звезды и ночь.
Проснулись люди, и увидели восходящее солнце, ибо лежали на боку, и полюбили солнце и день.
Проснулись дворфы, и не увидели ничего, ибо лежали носом в землю, и подумали: зачем же надо было вчера так напиваться?""",
    """Дворфийский анекдот: Вы называете свою цену. Я называю свою цену. Потом мы оба смеемся и приступаем к серьезному разговору.""",
    """Орк стрижет эльфа.
- Эльф, тебе уши нужны?
- Конечно.
- На, держи!""",
    """Дворф просит Эльфа
- Эльф, а Эльф, достань соловья что сидит на макушке дерева.
- Отстань, нагибаться не охота!""",
    """Первое правило паладина:
Интеллект настоящего паладина должен быть чуть выше,
чем у его меча. Иначе меч возьмет его под контроль. """,
    """Приходит мужик к Магу.
- У вас частые головные боли и вы отец двух детей - сказал ясновидец.
- Да, но я отец трех детей.
- Это вы так думаете.""",
    """Беседует эльф с орком:
- У тебя какое первое слово было?
- Да пошёл ты, ужастый!..
- А у меня - "мама"...""",

    """Идут дворф и эльф по лесу. Вдруг, эльф кричит гному:
- Дворф, дворф! Ты это видел???
- Нет, не видел. - Отвечает дворф.
- Как ты не видел??? Такая заря замечательная! Ты много упустил...
Идут дальше. Эльф опять обращается к дворф:
- Нет, слушай, ну ты это видел???
- Не видел, - буркнул дворф.
- Как, как ты мог этого не видеть??? Такая лань мимо пролетела, тонкая, как стрела... Ты много потерял...
Идут дальше. Эльф говорит дворф:
- Дворф!!!!!!!!!!! Ты ЭТО видел???
Тут дворф надоело.
- Ну видел, видел я...
Эльф:
- Так ты что, специально туда наступил??? """,

    """Орк - дитя природы. ласковый и милый, и не его вина что эльфы и прочие находятся ниже в пищевой цепочке.""",
    """ОРКестр - сборище орков, отчаянно пытающихся изобразить музыкальные инструменты.""",
    """Орки ушли на Север, и больше о них ничего не слышали.
Но, триста лет спустя, они начали один за другим появляться на Юге...
Так Мудрые узнали, что Земля круглая.""",
    """Приезжают дворфы торговать в деревню полуросликов. Лето, страшная жара. 
Заходят они и видят: орк водит хоббитов вокруг ёлки, все в шубы одеты. Дворфы обалдели, позвали этого орка и спрашивают:
- Что вы делаете! Сейчас же не зима!
- (со вздохом) Да не доживут они до зимы…""",
    """Оказывается, по орочьи "вегетарианец" означает "криворукий охотник"…""",
    """Один орк спрашивает у сосредоточённо жующего другого орка:
- Интересно, о чём ты сейчас думаешь?
- Ни о чём! У меня мышцы головы другим делом заняты.""",
    """Какую скорость может развить человек, если знает, что орк - голоден? """,
    """Мы, боты, очень любим читать биографии. И, вот, недавно в биографии очень смелого человека я прочитал фразу:
- Орки, вас боятся не потому что уважают, а потому что вы страшные.
Книга на этом кончилась""",
    """Поймал дворф золотую рыбку...
Смотрит она на него так внимательно-внимательно и говорит:
- Дворф ?
- Да
- Тогда лучше зажарь """,
    """«Тоже неплохо!» - сказал орк, кинув камень в эльфа и попав в человека. """,
    """Беседуют Орк и Гном:
Орк: - Орки лучше чем гномы.
Гном: - Ну чем, чем лучше?!!
Орк: - Чем гномы!""",
    """Купил себе эпический меч и не жалею.
Никого не жалею.""",
    """Командир орков: Мы вновь докажем силу нашего оружия!!!
Орки: Д-а-а-а-а-а!!!
Командир орков: Мы перережем всех эльфийских мужчин!!!
Орки: Д-а-а-а-а-а!!!
Командир орков: Мы надругаемся над эльфийскими женщинами!!!
Орки: Д-а-а-а-а-а!!!
Командир орков: Да смотрите, не перепутайте как в прошлый раз…
""",
    """Партия встречает на дороге бродячего торговца.
Файтер (здоровенный, в полтора обхвата, ящер): -Показывай, чего у тебя есть.
Торговец: - Ну вот, зелья всякие, стрелы, аптечки, немного оружия...
Файтер: -А это что за дрючок?
Торговец: -Это зачарованный меч эльфийской стали, стоит 1500 золотых.
Файтер: -Берём!
ДМ: -У вас нет таких денег.
Файтер: -А я не сказал "покупаем", я сказал "берём".""",
    """Партия стоит в раздумьях перед ужасным каменным оживающим монстром.
Рик: Я могу разбить ему голову!
Эльза: А я могу его подлечить!
Айла: А я могу быстро убежать!
Эльза: Да.. мы идеальная команда!""",
    """Заходит орк в деревню к полуросликам и говорит: 
- Десять хоббитов ко мне, быстро! 
Эльфы забегают с ним за горку, через пять минут орк опять выходит и говорит: 
- Пятнадцать хоббитов ко мне, быстро! 
Ну, хоббиты опять бегут, через пять минут орк выходит: 
- Двадцать хоббитов ко мне, быстро! 
Хоббиты забегают, через пять минут один хоббит, весь окровавленый, выползает и говорит: 
- Не ходите туда, там засада, их двое!!! """,
    """- Я нашел отличный способ напиваться на халяву - говорит один тролль другому. 
- Это как? 
- Приходишь в гости в полуросликам или людишкам и говоришь: 
"Что-то я нынче никак решить не могу: то ли выпить мне, то ли закусить?" И все тут же бегут к тебе с дармовой выпивкой.
""",
    """Эльфа спрашивают, что надо сделать для того, чтобы все были счастливы? 
- Во первых, истребить орков, а во вторых, раздать всем по арфе. 
- А зачем арфы? 
- Я так и знал, что по первому пункту возражений не будет.""",
    """Разговор двух орков:
- И откуда ж у тебя такой топор красивый? 
- Мне королева эльфов дала. 
- Круто! А топор откуда? """,
    """Два игрока из разных партий обсуждают последние события.
- Блин, у нас в партии маг был. Веселый чувак.
- А почему был?
- Так умер.
- Оу. Сочувствую. А как это произошло?
- Ну, мы пробрались в башню правителя тирана, убили его, но начался пожар.
- Так, так.
- Ну, вот. Вылезаем на балкон, кричим, что, дескать, тиран повержен, а теперь нас надо спасать. Народ прибежал, растянули батут, говорят, прыгайте.
Я рейнджер, ловкий и все такое. Прыгнул - жив, здоров. Файтер наш прыгнул, рога... И настала очередь мага. А он все не решается...
- Ох, сгорел?
- Да не, решился. Прыгнул на батут, кидает на атлетику - единица.
- Разбился?
- Да не. Потом акробатику кинул на 20 и извернувшись снова подлетел в воздух, да прямо на тот самый балкон.
- Так сгорел?
- Да не. Снова прыгнул. Опять единица.
- Разбился?
- Нет. Опять 20 и на балкон.
- Сгорел?
- Нет конечно. Опять прыгнул и...
- Давай покороче.
- Я его застрелил. Заколебал туда сюда летать.""",
    """Мастер: «…и стражник отказывается пропустить вас в Цитадель».
Игрок: «Могу я бросить на Дипломатию?»
Мастер: «Конечно, давай».
Игрок: «27».
Мастер: «Вау, действительно хороший результат. Ладно, это было здорово, а со стражником ты что-то делать собираешься?»
Игрок: «Ну, я думал воздействовать на него этим броском».
Мастер: «Хорошо, он тоже впечатлен твоим результатом. Однако он не взял с собой двадцатигранник и не сможет сыграть с тобой. Да и, откровенно говоря, он на работе и отвлекаться на подобные забавы сейчас вряд ли захочет».""",
    """Два орка едят клоуна. И один другого спрашивает:
— правда смешно?""",
    """... Рыцарь вбежал в комнату к красавице принцессе. Она рыдала:
— Завтра меня отдадут дракону, каждый год дракону отдают на съедение самую красивую девственницу города. А это я! Ну почему я такая красивая?!
— Я спасу тебя! — пылко ответил рыцарь.
— Ты убьешь дракона? — обрадовалась принцесса.
— Есть более простое решение, — ответил рыцарь, снимая штаны.
— А других простых способов нет? — поинтересовалась принцесса.
— Ну, еще можно сломать тебе нос и ты перестанешь быть самой красивой.
И принцесса стала снимать платье...""",
    """Судят орка за то что украл лошадь. Судья говорит: — Ты, животное немытое, что скажешь в свое оправдание?
     Орк рассказывает: — Иду я значит по улочке, никого не трогаю, смотрю — на дороге лошадь лежит, ну я ее с лева обойти — не получется, справа — не получается, места нет, ну думаю переступлю через нее и дальше пойду, только ногу поднял чтобы переступить, а она кааак понесется, хорошо, что господа стражи остановили...""",
    """Как бы Орк не пытался скрутить роллы, скручивает он все равно голову эльфу.""",
    """Один Орк спрашивает другого:
- Отчего умер дракон, который жил на нашей горе с незапамятных времен?
- Да от голода.
- Как это?
- Да съел я его...""",
    """Идёт война. Паладин из штаба и местный начальник Варвар проверяют в лагере запасы воды.
- Какие меры вы принимаете для профилактики инфекции?
- Сначала мы кипятим воду.
- Хорошо. А потом?
- Потом мы её фильтруем.
- Отлично. А что вы делаете дальше?
- А дальше, чтоб не рисковать, мы пьём водку...""",
    """Тёмная эльфийка танцует на балу с человеком.
- Дорогой, у Вас пятнышко на манжете, - делает замечание тёмная эльфийка.
Человек уходит в другую комнату и, не выдержав позора, вешается.
А дроу уже танцует с эльфом.
- Милейший, у Вас пятнышко на сюртуке, - делает замечание тёмная эльфийка.
Эльф уходит в другую комнату и, не выдержав позора, зарезывается.
И вот очередь орка.
- Уважаемый, да у Вас сапоги грязные...
- Hе беспокойтесь, мадам, это не грязь, а говно. Сейчас подсохнет и само отвалится...""",
    """Говорят, эльфы — это промежуточное звено между обезьяной и человеком: шерсть уже отвалилась, а с деревьев еще не слезли.""",
    """Поймал темный властелин Паладина, Волшебника и Вора. И говорит:
- Дам вам шанс спасти свою жизнь. И даже золота накину, если справитесь! На этой комнате лежит страшное заклятье и любой, кто соврёт - погибнет. А теперь, ответьте мне честно, какой из классов круче?
Первым стал отвечать вор:
- Я думаю, круче всех классов - вор...
И тот час ласты склеил. Вторым стал отвечать волшебник:
- Я думаю, лучше всех классов - волшебник...
И упал замертво. Пришла очередь паладина:
- Я думаю... 
И умер.""",
    """Пришел в библиотеку паладин.
- Дайте, мне, пожалуйста, книгу о самых умных паладинах.
- Фантастика в другом зале.""",
    """Делают гномы орку операцию на мозге. Вскрывают черепную коробку. Смотрят, а там всего три извилины. Две удалили, зашили, операция прошла успешно. Орк встает, подходит к зеркалу:
- Ух, какой из меня крутой паладин получился! """,
    """Два орка заметили барда, идущего через лес. Один говорит другому:
-Слушай, а давай его подколим!
- Давай, а как?
- Ну знач, подходим к нему, я начинаю: "Привет, а чего у тебя такой костюмчик голубой?".
Он там, чего нить промямлит. А ты продолжаешь: "Наверное нетрадиционная сексуальная ориентация!"
Ну поравнялись с бардом,
1-ый орк - Привет, а че у тя роба голубая?
Бард сходу - Привет, а вы чего тут среди ночи парочкой ходите?
2-ой орк - Ну дык эта... Нетрадиционная сексуальная ориентация!""",
    """Идёт паладин по вражьей территории. Но тут - засада, орки, тролли, гоблины - целая куча. Дальше затяжной бой и тысяча воинов все ж скрутила его.
- Ну все вот мне и конец - думает паладин.
- Нет! Тебе еше не конец!!! - Божественный голос сверху.
- О, великий, подскажи что мне сделать! - Взмолился тогда паладин.
- Выхвати кинжал у вождя тролей и убей им его сына! - Вещает голос.
Паладин в прыжке выхватывает кинжал у вождя и в одно мгновение убивает его сына после чего перекатом уходит в сторону.
Голос сверху отвечает:
- Вот теперь да, тебе точно конец.""",
    """Что нужно сделать, чтоб у паладина глаза загорелись? Посветить ему в ухо фонарём!""",
    """Прибегает девушка к Барду в таверну.
- Милый, прости! Вчера у тебя в комнате я забыла свои трусики, ты их не находил?
- Угу, нашёл!
- А что же ты мне сразу не отдал?
- А вдруг они не твои? """,
)

def getRofl():
    return str(rofles[rnd(len(rofles))])