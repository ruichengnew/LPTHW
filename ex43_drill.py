#Question 1
#我很想change it，但不是现在，我已经有了一个不错的猜想，我要写一个关于310宿舍的游戏

#Question 2
#因为从0开始猜，猜到9为止都会出发while-loop，还有一次不触发的机会，总共11次

#Question 3
#是这样
1. 首先定义了a_map，a_game,并运行了a_game.play()，这个play会触发engine中的while-loop
2. 这个loop的判定条件比较现在进行的scene和Finished（）这个场景，如果不一样就运行loop
3. 由于赋值了a_map所以，第一个scene是central，明显跟finished不一样，就运行loop中的第一行代码
4. 第一行代码会赋值一个next_scene，而想要赋值就必须调用enter函数给current_scene，于是就开始运行第一个游戏
5. 运行完第一个游戏会得到两个可能的返回值，一个是laser，一个是death
6. death返回值会赋值给next_scene，再call Map class中的next_scene函数得到下一个current_scene，也就是Death（），这时继续运行while-loop，就会发现death和finished也不一样，运行第一行时会触发enter函数，通过death中的exit（1）退出整个函数
7. 如果返回值是laser，那么laser就会赋值给next_scene，也会通过Map class call next_scene function，然后再while-loop，直到你能走到finished（）
8. 如果你成功到达finished，那么while-loop就被打断了，不运行了，就会接着play函数往下运行，current_scene.enter()，这个时候的current_scene == last_scene,也就是Finished（），enter之后print（“you win , good job”)

#过程其实很清楚了，但是在反复进出class和调用函数方面，我还是会犯错误

#Question 4
OK, 把我难到了，你赢了

#Question 5
#Ok，next times

#Question 6
#cool
