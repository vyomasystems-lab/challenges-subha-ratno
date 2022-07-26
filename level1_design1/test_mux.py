# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    #cocotb.log.info('##### CTB: Develop your test here ########')
    Sel = 5;
    In0 = 1;
    In1 = 3;
    In2 = 2;
    In3 = 3;
    In4 = 1;
    In5 = 3;
    In6 = 2;
    In7 = 2;
    In8 = 1;
    In9 = 0;
    In10 = 3;
    In11 = 3;
    In12 = 0;
    In13 = 1;
    In14 = 2;
    In15 = 0;
    In16 = 3;
    In17 = 1;
    In18 = 2;
    In19 = 3;
    In20 = 2;
    In21 = 2;
    In22 = 1;
    In23 = 1;
    In24 = 0;
    In25 = 1;
    In26 = 1;
    In27 = 2;
    In28 = 3;
    In29 = 3;
    In30 = 0;
    In31 = 3;

    #input driving
    dut.sel.value = Sel;
    dut.in0.value = In0;
    dut.in1.value = In1;
    dut.in2.value = In2;
    dut.in3.value = In3;
    dut.in4.value = In4;
    dut.in5.value = In5;
    dut.in6.value = In6;
    dut.in7.value = In7;
    dut.in8.value = In8;
    dut.in9.value = In9;
    dut.in10.value = In10;
    dut.in11.value = In11;
    dut.in12.value = In12;
    dut.in13.value = In13;
    dut.in14.value = In14;
    dut.in15.value = In15;
    dut.in16.value = In16;
    dut.in17.value = In17;
    dut.in18.value = In18;
    dut.in19.value = In19;
    dut.in20.value = In20;
    dut.in21.value = In21;
    dut.in22.value = In22;
    dut.in23.value = In23;
    dut.in24.value = In24;
    dut.in25.value = In25;
    dut.in26.value = In26;
    dut.in27.value = In27;
    dut.in28.value = In28;
    dut.in29.value = In29;
    dut.in30.value = In30;
    dut.in31.value = In31;

    #dut.out.value = Out;

    await Timer(2, units='ns')
    
    assert dut.out.value == In5, "MUX result is incorrect: for select = {sel}, output != {out}, expected value={EXP}".format(
            sel=int(dut.sel.value), out=int(dut.out.value), EXP=In5)