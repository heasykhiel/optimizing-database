from manim import *
class database(Scene):
    def construct(self):
        wel = Text('What is the best way to optimize your Database', font_size=28)
        self.play(
            Write(wel)
        )
        self.play(
            Unwrite(wel)
        )
        pr = Text('Stored Procedures:', font_size=28).shift(UL*3.7).shift(LEFT*1.7)
        self.play(
            Write(pr), run_time=0.5
        )
        
        r = Rectangle(height=3.5, width=4.5).set_color('#0485F600').set_fill('#0485F600',opacity=1)
        gr = VGroup(*[Rectangle(height=0.5, width=1.2) for _ in range(3)]).arrange(LEFT,buff=0.15).move_to(r).shift(UP*0.85).set_color(WHITE).set_fill(WHITE,opacity=1)
        gr1 = gr.copy().next_to(gr, DOWN *0.7)
        gr2 = gr.copy().next_to(gr1, DOWN *0.7)
        gr3 = gr.copy().next_to(gr2, DOWN *0.7)
        r_all = VGroup(r, gr, gr1, gr2, gr3)
        
        self.play(
            Create(r_all), run_time=0.5
        )
        self.play(
            r_all.animate.move_to(UL).shift(LEFT*2), run_time=0.5
        )
        
        tr = Text('GUI').next_to(r_all, UP).set_color('#1C99FF00')
        
        evy = VGroup(r_all, tr)
        
        self.play(
            Write(tr), run_time=0.5
        )
        
        
        c_a = CurvedArrow(
            RIGHT , LEFT, # Ending point
            radius=-2.5).scale(1.5).next_to(r_all, RIGHT*0.1).shift( RIGHT*0.01).shift(UP*0.9).rotate(180*DEGREES).set_color('#254C6F00')
        sl = Text('SQL Queries', font_size=18).next_to(c_a, UP*0.1).set_color('#1C99FF00')
        casl = VGroup(c_a, sl)
        
        self.play(
            Create(c_a), run_time=0.5
        )
        self.play(
            Write(sl), run_time=0.5
        )
        
        d_a = DoubleArrow(RIGHT, LEFT).scale(2).next_to(r_all, RIGHT*0.05).shift(RIGHT*0.01).set_color('#254C6F00')
        sl1 = Text('Stored Procedures', font_size=18).next_to(d_a, UP*0.1).set_color('#1C99FF00')
        dsl = VGroup(d_a, sl1)
        
        self.play(
            Create(d_a), run_time=0.5
        )
        self.play(
            Write(sl1), run_time=0.5
        )
        
        
        
        
        c_a1 = CurvedArrow(
            RIGHT , LEFT, 
            radius=-2.5).scale(1.5).next_to(r_all, RIGHT*0.1).shift( RIGHT*0.01).shift(DOWN*0.9).rotate(360*DEGREES).set_color('#254C6F00')
        sl2 = Text('Data', font_size=20).next_to(c_a1, DOWN*0.1).set_color('#1C99FF00')
        cs2 =VGroup(c_a1, sl2)
        
        self.play(
            Create(c_a1), run_time=0.5
        )
        self.play(
            Write(sl2), run_time=0.5
        )
        
        rec1 = Rectangle(height= 2,width = 2.5).scale(1.5)
        cc1 = Circle(radius=1.87).next_to(rec1.get_start()).stretch_to_fit_height(.6).shift(LEFT * 4)
        cc2 = cc1.copy().shift(DOWN * 3)
        re2 = VGroup(rec1,cc1,cc2).set_color([YELLOW, RED]).set_fill([YELLOW, RED],opacity=1).scale(0.7).next_to(c_a).shift(DOWN*0.9+LEFT*0.2)
        t = Text('Database', font='Monospace',font_size=28, weight=BOLD).move_to(rec1).set_color('#0485F600')
        
        rect = VGroup(re2, t)
        
        self.play(
            GrowFromCenter(re2), run_time=0.5
        )
        self.play(
            Write(t), run_time=0.5
        )
        allitem = VGroup(evy, casl, dsl, cs2,rect)
        
        self.wait(1)
       
        self.play(
            
            FadeOut(pr,allitem), run_time=0.5
        )
        
        
        ex =Text("Here's an example of a simple stored procedure written in SQL Server:", font_size=28).shift(UL*3.65).shift(RIGHT*2.35)
        self.play(
            Write(ex), run_time=0.5
        )
        
        rc = Rectangle(height=3, width=8).shift(UP*1.5).set_color('#11111100').set_fill('#13121A00',opacity=1)
        rc1 = Rectangle(height=0.7, width=8).move_to(rc.get_start()).shift(DOWN*0.35, LEFT*4).set_color('#11111100').set_fill('#19191B00',opacity=1)
        rc2 = Rectangle(height=0.5, width=3).move_to(rc.get_start()).shift(DOWN*0.48, LEFT*6).set_color('#13121A00').set_fill('#13121A00',opacity=1)
        dot = VGroup(*[Dot(radius=0.2).scale(.5) for _ in range(3)]).arrange(LEFT,buff=0.1).move_to(rc1).shift(RIGHT*3.2)
        dot[2].set_color(RED)
        dot[1].set_color(YELLOW)
        dot[0].set_color(GREEN)
        tx = Text('Stored Procedures', font_size=18).set_color('#97919100').move_to(rc2)
        rrd =VGroup(rc,rc1,rc2,dot,tx)
        
        self.play(
            Create(rrd), run_time=0.5
        )
        
        
        inp = Text('CREATE  PROCEDURE  GetEmployeeById', font_size=16).move_to(rc).shift(UP*0.4, LEFT*1.8)
        inp[:15].set_color('#A23F6500')
        inp[15:].set_color('#97919100')
        inp1 = Text('@EmployeeId   INT', font_size=16).next_to(inp, DOWN*0.55).shift(LEFT*0.5)
        inp1[:11].set_color('#97919100')
        inp1[11:].set_color('#A23F6500')
        inp2 = Text('AS', font_size=16).next_to(inp1, DOWN*0.55).shift(LEFT*1.3).set_color('#A23F6500')
        inp3 = Text('BEGIN', font_size=16).next_to(inp2, DOWN*0.55).shift(LEFT*0.05 +RIGHT*0.25).set_color('#A23F6500')
        inp4 = Text('SELECT  *  FROM Employees WHERE EmployeeId = @EmployeeId;', font_size=16).next_to(inp3, DOWN*0.55).shift(LEFT*0.05 +RIGHT*3.25)
        inp4[:11].set_color('#A23F6500')
        inp4[11:20].set_color('#97919100')
        inp4[20:25].set_color('#A23F6500')
        inp4[25:35].set_color('#97919100')
        inp4[35].set_color('#A23F6500')
        inp4[35:].set_color('#97919100')
        inp5 = Text('END;', font_size=16).next_to(inp4, DOWN*0.55).shift(LEFT*3.27)
        inp5[:3].set_color('#A23F6500')
        alltext = VGroup(inp,inp1,inp2,inp3,inp4,inp5)
        
        for i in alltext:
            for char in i:
                 self.play(
                Write(char), run_time=0.1
            )
                
           
        cda = CurvedDoubleArrow(
            start_point=LEFT,  # Starting point
            end_point=RIGHT,   # Ending point
            radius=1.7, tip_length= 0.2).next_to(rc, DOWN*3).shift(LEFT*2).scale(0.9).rotate(-70*DEGREES).set_color('#254C6F00')
        
        self.play(
            Create(cda), run_time=0.5
        )
    

        data = rect.copy().next_to(cda).shift(DOWN+LEFT*0.1)
        self.play(
            FadeIn(data), run_time=0.5
        )
        self.wait(1)
        
        self.play(
            FadeOut(ex,rrd,alltext,cda), run_time=0.5
        )
        
        
        fn = Text('Once the stored procedure is created, you can call it like this:', font_size=28).shift(UL*3.45).shift(UP*0.2).shift(RIGHT*1.3)
        self.play(
            Write(fn), run_time=0.5
        )
        
        self.play(
            data.animate.move_to(UP*2), run_time=0.5
        )
        
        car1 = CurvedArrow(UP, DOWN, radius=1.7, tip_length= 0.2).next_to(data).shift(LEFT*3.3 +DOWN*1.3).set_color('#254C6F00')
        self.play(
            Create(car1), run_time=0.5
        )
        
        cl2 = Text('Data', font_size=24).next_to(car1).set_color('#1C99FF00').shift(LEFT*0.1 +DOWN*0.5)
        self.play(
            Write(cl2), run_time=0.5
        )
        crc = Rectangle(height=3, width=8).shift(UP*1.5).set_color('#11111100').set_fill('#13121A00',opacity=1)
        crc1 = Rectangle(height=0.7, width=8).move_to(crc.get_start()).shift(DOWN*0.35, LEFT*4).set_color('#11111100').set_fill('#19191B00',opacity=1)
        crc2 = Rectangle(height=0.5, width=3).move_to(crc.get_start()).shift(DOWN*0.48, LEFT*6).set_color('#13121A00').set_fill('#13121A00',opacity=1)
        cdot = VGroup(*[Dot(radius=0.2).scale(.5) for _ in range(3)]).arrange(LEFT,buff=0.1).move_to(crc1).shift(RIGHT*3.2)
        cdot[2].set_color(RED)
        cdot[1].set_color(YELLOW)
        cdot[0].set_color(GREEN)
        ctx = Text('Stored Procedures', font_size=18).set_color('#97919100').move_to(crc2)
        crrd =VGroup(crc,crc1,crc2,cdot,ctx).next_to(car1.get_end()).shift(DOWN*1.5 +LEFT*4)
        
        self.play(
            Create(crrd), run_time=0.5
        )
        
        enp = Text('EXEC  GetEmployeeById  @EmployeeId  =  123;', font_size=16).move_to(crc)
        enp[:4].set_color('#A23F6500')
        enp[4:30].set_color('#97919100')
        enp[30].set_color('#A23F6500')
        enp[31:34].set_color('#DA72F700')
        enp[34].set_color('#97919100')
        
        
        for i in enp:
            self.play(
                Write(i), run_time=0.1
            )
        
       
        
    
        
        self.wait(3)
        
        
       