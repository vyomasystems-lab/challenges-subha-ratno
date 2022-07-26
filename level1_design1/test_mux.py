# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_basic1(dut):
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

    #input driving
    dut.sel.value = Sel;
    dut.inp0.value = In0;
    dut.inp1.value = In1;
    dut.inp2.value = In2;
    dut.inp3.value = In3;
    dut.inp4.value = In4;
    dut.inp5.value = In5;
    dut.inp6.value = In6;
    dut.inp7.value = In7;
    dut.inp8.value = In8;
    dut.inp9.value = In9;
    dut.inp10.value = In10;
    dut.inp11.value = In11;
    dut.inp12.value = In12;
    dut.inp13.value = In13;
    dut.inp14.value = In14;
    dut.inp15.value = In15;
    dut.inp16.value = In16;
    dut.inp17.value = In17;
    dut.inp18.value = In18;
    dut.inp19.value = In19;
    dut.inp20.value = In20;
    dut.inp21.value = In21;
    dut.inp22.value = In22;
    dut.inp23.value = In23;
    dut.inp24.value = In24;
    dut.inp25.value = In25;
    dut.inp26.value = In26;
    dut.inp27.value = In27;
    dut.inp28.value = In28;
    dut.inp29.value = In29;
    dut.inp30.value = In30;

    await Timer(2, units='ns')
    
    assert dut.out.value == In5, "MUX result is incorrect: for select = {sel}, output != {out}, expected value={EXP}".format(
            sel=int(dut.sel.value), out=int(dut.out.value), EXP=In5)

@cocotb.test()
async def test_mux_basic2(dut):
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

    #input driving
    dut.sel.value = Sel;
    dut.inp0.value = In0;
    dut.inp1.value = In1;
    dut.inp2.value = In2;
    dut.inp3.value = In3;
    dut.inp4.value = In4;
    dut.inp5.value = In5;
    dut.inp6.value = In6;
    dut.inp7.value = In7;
    dut.inp8.value = In8;
    dut.inp9.value = In9;
    dut.inp10.value = In10;
    dut.inp11.value = In11;
    dut.inp12.value = In12;
    dut.inp13.value = In13;
    dut.inp14.value = In14;
    dut.inp15.value = In15;
    dut.inp16.value = In16;
    dut.inp17.value = In17;
    dut.inp18.value = In18;
    dut.inp19.value = In19;
    dut.inp20.value = In20;
    dut.inp21.value = In21;
    dut.inp22.value = In22;
    dut.inp23.value = In23;
    dut.inp24.value = In24;
    dut.inp25.value = In25;
    dut.inp26.value = In26;
    dut.inp27.value = In27;
    dut.inp28.value = In28;
    dut.inp29.value = In29;
    dut.inp30.value = In30;

    await Timer(2, units='ns')
    
    assert dut.out.value == In5, "MUX result is incorrect: for select = {sel}, output != {out}, expected value={EXP}".format(
            sel=int(dut.sel.value), out=int(dut.out.value), EXP=In5)

# @cocotb.test()
# async def test_mux_randomised(dut):
#     """Test for mux2"""

#     #cocotb.log.info('##### CTB: Develop your test here ########')
#     Sel = 5;
#     In0 = 1;
#     In1 = 3;
#     In2 = 2;
#     In3 = 3;
#     In4 = 1;
#     In5 = 3;
#     In6 = 2;
#     In7 = 2;
#     In8 = 1;
#     In9 = 0;
#     In10 = 3;
#     In11 = 3;
#     In12 = 0;
#     In13 = 1;
#     In14 = 2;
#     In15 = 0;
#     In16 = 3;
#     In17 = 1;
#     In18 = 2;
#     In19 = 3;
#     In20 = 2;
#     In21 = 2;
#     In22 = 1;
#     In23 = 1;
#     In24 = 0;
#     In25 = 1;
#     In26 = 1;
#     In27 = 2;
#     In28 = 3;
#     In29 = 3;
#     In30 = 0;

#     #input driving
#     dut.sel.value = Sel;
#     dut.inp0.value = In0;
#     dut.inp1.value = In1;
#     dut.inp2.value = In2;
#     dut.inp3.value = In3;
#     dut.inp4.value = In4;
#     dut.inp5.value = In5;
#     dut.inp6.value = In6;
#     dut.inp7.value = In7;
#     dut.inp8.value = In8;
#     dut.inp9.value = In9;
#     dut.inp10.value = In10;
#     dut.inp11.value = In11;
#     dut.inp12.value = In12;
#     dut.inp13.value = In13;
#     dut.inp14.value = In14;
#     dut.inp15.value = In15;
#     dut.inp16.value = In16;
#     dut.inp17.value = In17;
#     dut.inp18.value = In18;
#     dut.inp19.value = In19;
#     dut.inp20.value = In20;
#     dut.inp21.value = In21;
#     dut.inp22.value = In22;
#     dut.inp23.value = In23;
#     dut.inp24.value = In24;
#     dut.inp25.value = In25;
#     dut.inp26.value = In26;
#     dut.inp27.value = In27;
#     dut.inp28.value = In28;
#     dut.inp29.value = In29;
#     dut.inp30.value = In30;

#     await Timer(2, units='ns')
    
#     assert dut.out.value == In5, "MUX result is incorrect: for select = {sel}, output != {out}, expected value={EXP}".format(
#             sel=int(dut.sel.value), out=int(dut.out.value), EXP=In5)
