#include <math.h>

int check_if_double_is_nan(double value) {
    return isnan(value);
}


void init_history(int lg, double* history){
    if (lg == 0){
        history[117] = 0;
        history[118] = -INFINITY;
        history[119] = 0;
        history[120] = 0;
        history[121] = 0;
        history[122] = 0;
        history[123] = 0;
        history[124] = 0;
        history[125] = 0;
        history[126] = 0;
        history[127] = 0;
        history[128] = 0;
        history[129] = 0;
        history[130] = 0;
        history[131] = 0;
        history[132] = 0;
        history[133] = 0;
        history[134] = 0;
        history[135] = -INFINITY;
        history[136] = 0;
        history[137] = 0;
        history[138] = 0;
        history[139] = 0;
        history[140] = 0;
        history[141] = 0;
        history[142] = 0;
        history[143] = 0;
        history[144] = 0;
        history[145] = 0;
        history[146] = -INFINITY;
        history[147] = 0;
        history[148] = 0;
        history[149] = -INFINITY;
        history[150] = 0;
        history[151] = 0;
        history[152] = 0;
        history[153] = 0;
        history[154] = 0;
        history[155] = INFINITY;
        history[156] = 0;
        history[157] = INFINITY;
        history[158] = -INFINITY;
        history[159] = 0;
        history[160] = 0;
        history[161] = INFINITY;
        history[162] = -INFINITY;
        history[163] = 0;
        history[164] = 0;
        history[165] = 0;
        history[166] = INFINITY;
        history[167] = 0;
        history[168] = 0;
        history[169] = 0;
        history[170] = 0;
        history[171] = 0;
        history[172] = -INFINITY;
        history[173] = 0;
        history[174] = 0;
        history[175] = 0;
        history[176] = INFINITY;
        history[177] = 0;
        history[178] = -INFINITY;
        history[179] = 0;
        history[180] = 0;
        history[181] = INFINITY;
        history[182] = 0;
        history[183] = INFINITY;
        history[184] = 0;
        history[185] = 0;
        history[186] = INFINITY;
        history[187] = 0;
        history[188] = 0;
        history[189] = 0;
        history[190] = 0;
        history[191] = INFINITY;
        history[192] = 0;
        history[193] = INFINITY;
        history[194] = 0;
        history[195] = 0;
        history[196] = INFINITY;
        history[197] = 0;
        history[198] = -INFINITY;
        history[199] = 0;
        history[200] = 0;
        history[201] = 0;
        history[202] = 0;
        history[203] = 0;
        history[204] = 0;
        history[205] = INFINITY;
        history[206] = -INFINITY;
        history[207] = 0;
        history[208] = 0;
        history[209] = INFINITY;
        history[210] = 0;
        history[211] = INFINITY;
        history[212] = -INFINITY;
        history[213] = 0;
        history[214] = 0;
        history[215] = 0;
        history[216] = 0;
        history[217] = 0;
        history[218] = 0;
        history[219] = 0;
        history[220] = 0;
        history[221] = 0;
        history[222] = -INFINITY;
        history[223] = 0;
        history[224] = 0;
        history[225] = 0;
        history[226] = 0;
        history[227] = -INFINITY;
        history[228] = 0;
        history[229] = 0;
        history[230] = 0;
        history[231] = 0;
        history[232] = 0;
        history[233] = 0;
        history[234] = 0;
        history[235] = -INFINITY;
        history[236] = 0;
        history[237] = INFINITY;
        history[238] = 0;
        history[239] = -INFINITY;
        history[240] = 0;
        history[241] = 0;
        history[242] = INFINITY;
        history[243] = 0;
        history[244] = 0;
        history[245] = 0;
        history[246] = INFINITY;
        history[247] = -INFINITY;
        history[248] = 0;
        history[249] = -INFINITY;
        history[250] = 0;
        history[251] = 0;
        history[252] = 0;
        history[253] = 0;
        history[254] = 0;
        history[255] = INFINITY;
        history[256] = -INFINITY;
        history[257] = 0;
        history[258] = 0;
        history[259] = 0;
        history[260] = 0;
        history[261] = -INFINITY;
        history[262] = 0;
        history[263] = 0;
        history[264] = 0;
        history[265] = INFINITY;
        history[266] = 0;
        history[267] = 0;
        history[268] = 0;
        history[269] = NAN;
        history[270] = NAN;
        history[271] = 0;
        history[272] = NAN;
        history[273] = NAN;
        history[274] = 0;
        history[275] = NAN;
        history[276] = NAN;
        history[277] = 0;
        history[278] = NAN;
        history[279] = 0;
        history[280] = NAN;
        history[281] = NAN;
        history[282] = 0;
        history[283] = NAN;
        history[284] = NAN;
        history[285] = 0;
        history[286] = NAN;
        history[287] = 0;
        history[288] = NAN;
        history[289] = 0;
        history[290] = NAN;
        history[291] = NAN;
        history[292] = 0;
        history[293] = NAN;
        history[294] = 0;
        history[295] = NAN;
        history[296] = NAN;
        history[297] = 0;
        history[298] = NAN;
        history[299] = 0;
        history[300] = NAN;
        history[301] = NAN;
        history[302] = 0;
        history[303] = NAN;
        history[304] = 0;
        history[305] = NAN;
        history[306] = NAN;
        history[307] = 0;
        history[308] = NAN;
        history[309] = 0;
        history[310] = NAN;
        history[311] = 0;
        history[312] = NAN;
        history[313] = NAN;
        history[314] = 0;
        history[315] = NAN;
        history[316] = 0;
        history[317] = NAN;
        history[318] = NAN;
        history[319] = 0;
        history[320] = NAN;
        history[321] = NAN;
        history[322] = 0;
        history[323] = NAN;
        history[324] = NAN;
        history[325] = 0;
        history[326] = NAN;
        history[327] = NAN;
        history[328] = 0;
        history[329] = NAN;
        history[330] = NAN;
        history[331] = 0;
        history[332] = NAN;
        history[333] = 0;
        history[334] = NAN;
        history[335] = 0;
        history[336] = NAN;
        history[337] = 0;
        history[338] = NAN;
        history[339] = NAN;
        history[340] = 0;
        history[341] = NAN;
        history[342] = NAN;
        history[343] = 0;
        history[344] = NAN;
        history[345] = NAN;
        history[346] = 0;
        history[347] = NAN;
        history[348] = 0;
        history[349] = NAN;
        history[350] = NAN;
        history[351] = 0;
        history[352] = NAN;
        history[353] = 0;
        history[354] = NAN;
        history[355] = NAN;
        history[356] = 0;
        history[357] = NAN;
        history[358] = 0;
        history[359] = NAN;
        history[360] = 0;
        history[361] = NAN;
        history[362] = 0;
        history[363] = NAN;
        history[364] = 0;
        history[365] = NAN;
        history[366] = 0;
        history[367] = NAN;
        history[368] = 0;
        history[369] = NAN;
        history[370] = NAN;
        history[371] = 0;
        history[372] = NAN;
        history[373] = 0;
        history[374] = NAN;
        history[375] = NAN;
        history[376] = 0;
        history[377] = NAN;
        history[378] = 0;
        history[379] = NAN;
        history[380] = NAN;
        history[381] = 0;
        history[382] = NAN;
        history[383] = 0;
        history[384] = NAN;
        history[385] = 0;
        history[386] = NAN;
        history[387] = 0;
        history[388] = NAN;
        history[389] = 0;
        history[390] = NAN;
        history[391] = 0;
        history[392] = NAN;
        history[393] = 0;
        history[394] = NAN;
        history[395] = 0;
        history[396] = NAN;
        history[397] = NAN;
        history[398] = 0;
        history[399] = NAN;
        history[400] = 0;
        history[401] = NAN;
        history[402] = 0;
        history[403] = NAN;
        history[404] = 0;
        history[405] = NAN;
        history[406] = 0;
        history[407] = NAN;
        history[408] = 0;
        history[409] = NAN;
        history[410] = 0;
        history[411] = NAN;
        history[412] = 0;
        history[413] = NAN;
        history[414] = NAN;
        history[415] = 0;
        history[416] = NAN;
        history[417] = 0;
        history[418] = NAN;
        history[419] = 0;
        history[420] = NAN;
        history[421] = 0;
        history[422] = NAN;
        history[423] = 0;
        history[424] = NAN;
        history[425] = NAN;
        history[426] = 0;
        history[427] = NAN;
        history[428] = NAN;
        history[429] = 0;
        history[430] = NAN;
        history[431] = 0;
        history[432] = NAN;
        history[433] = NAN;
        history[434] = 0;
        history[435] = NAN;
        history[436] = 0;
        history[437] = NAN;
        history[438] = NAN;
        history[439] = 0;
        history[440] = NAN;
        history[441] = 0;
        history[442] = NAN;
        history[443] = NAN;
        history[444] = 0;
        history[445] = NAN;
        history[446] = 0;
        history[447] = NAN;
        history[448] = 0;
        history[449] = NAN;
        history[450] = 0;
        history[451] = NAN;
        history[452] = 0;
        history[453] = NAN;
        history[454] = 0;
        history[455] = NAN;
        history[456] = 0;
        history[457] = NAN;
        history[458] = NAN;
        history[459] = 0;
        history[460] = NAN;
        history[461] = 0;
        history[462] = NAN;
        history[463] = 0;
        history[464] = NAN;
        history[465] = NAN;
        history[466] = 0;
        history[467] = NAN;
        history[468] = NAN;
        history[469] = 0;
        history[470] = NAN;
        history[471] = 0;
        history[472] = NAN;
        history[473] = 0;
        history[474] = NAN;
        history[475] = 0;
        history[476] = NAN;
        history[477] = NAN;
        history[478] = 0;
        history[479] = NAN;
        history[480] = 0;
        history[481] = NAN;
        history[482] = 0;
        history[483] = NAN;
        history[484] = NAN;
        history[485] = 0;
        history[486] = NAN;
        history[487] = 0;
        history[488] = NAN;
        history[489] = 0;
        history[490] = NAN;
        history[491] = 0;
        history[492] = NAN;
        history[493] = 0;
        history[494] = NAN;
        history[495] = NAN;
        history[496] = 0;
        history[497] = NAN;
        history[498] = NAN;
        history[499] = 0;
        history[500] = NAN;
        history[501] = 0;
        history[502] = NAN;
        history[503] = 0;
        history[504] = NAN;
        history[505] = NAN;
        history[506] = 0;
        history[507] = NAN;
        history[508] = 0;
        history[509] = NAN;
        history[510] = NAN;
        history[511] = 0;
        history[512] = NAN;
        history[513] = NAN;
        history[514] = 0;
        history[515] = NAN;
        history[516] = NAN;
        history[517] = 0;
        history[518] = NAN;
        history[519] = NAN;
        history[520] = 0;
        history[521] = NAN;
        history[522] = 0;
        history[523] = NAN;
        history[524] = NAN;
        history[525] = 0;
        history[526] = NAN;
        history[527] = 0;
        history[528] = NAN;
        history[529] = NAN;
        history[530] = 0;
        history[531] = NAN;
        history[532] = 0;
        history[533] = NAN;
        history[534] = NAN;
        history[535] = 0;
        history[536] = NAN;
        history[537] = 0;
        history[538] = NAN;
        history[539] = 0;
        history[540] = NAN;
        history[541] = NAN;
        history[542] = 0;
        history[543] = NAN;
        history[544] = 0;
        history[545] = NAN;
        history[546] = 0;
        history[547] = NAN;
        history[548] = 0;
        history[549] = NAN;
        history[550] = 0;
        history[551] = NAN;
        history[552] = NAN;
        history[553] = 0;
        history[554] = NAN;
        history[555] = 0;
        history[556] = NAN;
        history[557] = 0;
        history[558] = NAN;
        history[559] = NAN;
        history[560] = 0;
        history[561] = NAN;
        history[562] = NAN;
        history[563] = 0;
        history[564] = NAN;
        history[565] = 0;
        history[566] = NAN;
        history[567] = 0;
        history[568] = NAN;
        history[569] = NAN;
        history[570] = 0;
        history[571] = NAN;
        history[572] = NAN;
        history[573] = 0;
        history[574] = NAN;
        history[575] = NAN;
        history[576] = 0;
        history[577] = NAN;
        history[578] = 0;
        history[579] = NAN;
        history[580] = 0;
        history[581] = NAN;
        history[582] = NAN;
        history[583] = 0;
        history[584] = NAN;
        history[585] = 0;
        history[586] = NAN;
        history[587] = 0;
        history[588] = NAN;
        history[589] = 0;
        history[590] = NAN;
        history[591] = 0;
        history[592] = NAN;
        history[593] = 0;
        history[594] = NAN;
        history[595] = 0;
        history[596] = NAN;
        history[597] = 0;
        history[598] = NAN;
        history[599] = 0;
        history[600] = NAN;
        history[601] = 0;
        history[602] = NAN;
        history[603] = 0;
        history[604] = NAN;
        history[605] = 0;
        history[606] = NAN;
        history[607] = 0;
        history[608] = NAN;
        history[609] = 0;
        history[610] = NAN;
        history[611] = 0;
        history[612] = 0;
        history[613] = NAN;
        history[614] = 0;
        history[615] = NAN;
        history[616] = 0;
        history[617] = NAN;
        history[618] = 0;
        history[619] = NAN;
        history[620] = NAN;
        history[621] = 0;
        history[622] = NAN;
        history[623] = NAN;
        history[624] = 0;
        history[625] = NAN;
        history[626] = 0;
        history[627] = NAN;
        history[628] = 0;
        history[629] = NAN;
        history[630] = NAN;
        history[631] = 0;
        history[632] = NAN;
        history[633] = 0;
        history[634] = NAN;
        history[635] = 0;
        history[636] = NAN;
        history[637] = 0;
        history[638] = NAN;
        history[639] = 0;
        history[640] = NAN;
        history[641] = 0;
        history[642] = NAN;
        history[643] = NAN;
        history[644] = 0;
        history[645] = NAN;
        history[646] = NAN;
        history[647] = 0;
        history[648] = NAN;
        history[649] = 0;
        history[650] = NAN;
        history[651] = NAN;
        history[652] = 0;
        history[653] = NAN;
        history[654] = 0;
        history[655] = NAN;
        history[656] = NAN;
        history[657] = 0;
        history[658] = NAN;
        history[659] = 0;
        history[660] = NAN;
        history[661] = 0;
        history[662] = 0;
        history[663] = 0;
    } else if (lg == 1){
        history[664] = 0;
        history[665] = -INFINITY;
        history[666] = 0;
        history[667] = 0;
        history[668] = 0;
        history[669] = 0;
        history[670] = 0;
        history[671] = 0;
        history[672] = 0;
        history[673] = 0;
        history[674] = 0;
        history[675] = 0;
        history[676] = -INFINITY;
        history[677] = 0;
        history[678] = -INFINITY;
        history[679] = 0;
        history[680] = 0;
        history[681] = 0;
        history[682] = -INFINITY;
        history[683] = 0;
        history[684] = INFINITY;
        history[685] = -INFINITY;
        history[686] = 0;
        history[687] = 0;
        history[688] = -INFINITY;
        history[689] = 0;
        history[690] = 0;
        history[691] = 0;
        history[692] = 0;
        history[693] = 0;
        history[694] = -INFINITY;
        history[695] = 0;
        history[696] = 0;
        history[697] = 0;
        history[698] = INFINITY;
        history[699] = 0;
        history[700] = 0;
        history[701] = 0;
        history[702] = -INFINITY;
        history[703] = 0;
        history[704] = 0;
        history[705] = -INFINITY;
        history[706] = 0;
        history[707] = 0;
        history[708] = 0;
        history[709] = 0;
        history[710] = 0;
        history[711] = 0;
        history[712] = 0;
        history[713] = 0;
        history[714] = 0;
        history[715] = 0;
        history[716] = -INFINITY;
        history[717] = 0;
        history[718] = 0;
        history[719] = -INFINITY;
        history[720] = 0;
        history[721] = 0;
        history[722] = 0;
        history[723] = INFINITY;
        history[724] = -INFINITY;
        history[725] = 0;
        history[726] = 0;
        history[727] = 0;
        history[728] = INFINITY;
        history[729] = 0;
        history[730] = -INFINITY;
        history[731] = 0;
        history[732] = 0;
        history[733] = 0;
        history[734] = -INFINITY;
        history[735] = 0;
        history[736] = 0;
        history[737] = 0;
        history[738] = -INFINITY;
        history[739] = 0;
        history[740] = 0;
        history[741] = -INFINITY;
        history[742] = 0;
        history[743] = 0;
        history[744] = INFINITY;
        history[745] = -INFINITY;
        history[746] = 0;
        history[747] = 0;
        history[748] = INFINITY;
        history[749] = 0;
        history[750] = INFINITY;
        history[751] = -INFINITY;
        history[752] = 0;
        history[753] = 0;
        history[754] = 0;
        history[755] = 0;
        history[756] = 0;
        history[757] = 0;
        history[758] = 0;
        history[759] = INFINITY;
        history[760] = -INFINITY;
        history[761] = 0;
        history[762] = 0;
        history[763] = INFINITY;
        history[764] = 0;
        history[765] = 0;
        history[766] = INFINITY;
        history[767] = 0;
        history[768] = 0;
        history[769] = INFINITY;
        history[770] = 0;
        history[771] = 0;
        history[772] = 0;
        history[773] = -INFINITY;
        history[774] = 0;
        history[775] = 0;
        history[776] = 0;
        history[777] = 0;
        history[778] = 0;
        history[779] = 0;
        history[780] = 0;
        history[781] = INFINITY;
        history[782] = 0;
        history[783] = -INFINITY;
        history[784] = 0;
        history[785] = 0;
        history[786] = 0;
        history[787] = 0;
        history[788] = -INFINITY;
        history[789] = 0;
        history[790] = 0;
        history[791] = -INFINITY;
        history[792] = 0;
        history[793] = 0;
        history[794] = 0;
        history[795] = 0;
        history[796] = 0;
        history[797] = 0;
        history[798] = 0;
        history[799] = -INFINITY;
        history[800] = 0;
        history[801] = 0;
        history[802] = -INFINITY;
        history[803] = 0;
        history[804] = INFINITY;
        history[805] = 0;
        history[806] = 0;
        history[807] = 0;
        history[808] = 0;
        history[809] = 0;
        history[810] = 0;
        history[811] = 0;
        history[812] = INFINITY;
        history[813] = -INFINITY;
        history[814] = 0;
        history[815] = 0;
        history[816] = 0;
        history[817] = INFINITY;
        history[818] = -INFINITY;
        history[819] = 0;
        history[820] = 0;
        history[821] = 0;
        history[822] = INFINITY;
        history[823] = -INFINITY;
        history[824] = 0;
        history[825] = 0;
        history[826] = INFINITY;
        history[827] = -INFINITY;
        history[828] = 0;
        history[829] = 0;
        history[830] = 0;
        history[831] = INFINITY;
        history[832] = 0;
        history[833] = 0;
        history[834] = -INFINITY;
        history[835] = 0;
        history[836] = 0;
        history[837] = 0;
        history[838] = INFINITY;
        history[839] = 0;
        history[840] = -INFINITY;
        history[841] = 0;
        history[842] = 0;
        history[843] = -INFINITY;
        history[844] = 0;
        history[845] = INFINITY;
        history[846] = 0;
        history[847] = 0;
        history[848] = 0;
        history[849] = 0;
        history[850] = INFINITY;
        history[851] = 0;
        history[852] = 0;
        history[853] = NAN;
        history[854] = NAN;
        history[855] = 0;
        history[856] = NAN;
        history[857] = 0;
        history[858] = NAN;
        history[859] = NAN;
        history[860] = 0;
        history[861] = NAN;
        history[862] = 0;
        history[863] = NAN;
        history[864] = NAN;
        history[865] = 0;
        history[866] = NAN;
        history[867] = 0;
        history[868] = NAN;
        history[869] = NAN;
        history[870] = 0;
        history[871] = NAN;
        history[872] = NAN;
        history[873] = 0;
        history[874] = NAN;
        history[875] = 0;
        history[876] = NAN;
        history[877] = 0;
        history[878] = NAN;
        history[879] = 0;
        history[880] = NAN;
        history[881] = 0;
        history[882] = NAN;
        history[883] = 0;
        history[884] = NAN;
        history[885] = NAN;
        history[886] = 0;
        history[887] = NAN;
        history[888] = NAN;
        history[889] = 0;
        history[890] = NAN;
        history[891] = NAN;
        history[892] = 0;
        history[893] = NAN;
        history[894] = 0;
        history[895] = NAN;
        history[896] = 0;
        history[897] = NAN;
        history[898] = NAN;
        history[899] = 0;
        history[900] = NAN;
        history[901] = 0;
        history[902] = NAN;
        history[903] = NAN;
        history[904] = 0;
        history[905] = NAN;
        history[906] = NAN;
        history[907] = 0;
        history[908] = NAN;
        history[909] = 0;
        history[910] = NAN;
        history[911] = NAN;
        history[912] = 0;
        history[913] = NAN;
        history[914] = NAN;
        history[915] = 0;
        history[916] = NAN;
        history[917] = 0;
        history[918] = NAN;
        history[919] = NAN;
        history[920] = 0;
        history[921] = NAN;
        history[922] = NAN;
        history[923] = 0;
        history[924] = NAN;
        history[925] = 0;
        history[926] = NAN;
        history[927] = 0;
        history[928] = NAN;
        history[929] = NAN;
        history[930] = 0;
        history[931] = NAN;
        history[932] = NAN;
        history[933] = 0;
        history[934] = NAN;
        history[935] = 0;
        history[936] = NAN;
        history[937] = NAN;
        history[938] = 0;
        history[939] = NAN;
        history[940] = 0;
        history[941] = NAN;
        history[942] = NAN;
        history[943] = 0;
        history[944] = NAN;
        history[945] = NAN;
        history[946] = 0;
        history[947] = NAN;
        history[948] = 0;
        history[949] = NAN;
        history[950] = 0;
        history[951] = NAN;
        history[952] = NAN;
        history[953] = 0;
        history[954] = NAN;
        history[955] = 0;
        history[956] = NAN;
        history[957] = 0;
        history[958] = NAN;
        history[959] = 0;
        history[960] = NAN;
        history[961] = NAN;
        history[962] = 0;
        history[963] = NAN;
        history[964] = 0;
        history[965] = NAN;
        history[966] = 0;
        history[967] = NAN;
        history[968] = 0;
        history[969] = NAN;
        history[970] = 0;
        history[971] = NAN;
        history[972] = 0;
        history[973] = NAN;
        history[974] = NAN;
        history[975] = 0;
        history[976] = NAN;
        history[977] = NAN;
        history[978] = 0;
        history[979] = NAN;
        history[980] = NAN;
        history[981] = 0;
        history[982] = NAN;
        history[983] = 0;
        history[984] = NAN;
        history[985] = 0;
        history[986] = NAN;
        history[987] = 0;
        history[988] = NAN;
        history[989] = 0;
        history[990] = NAN;
        history[991] = 0;
        history[992] = NAN;
        history[993] = 0;
        history[994] = NAN;
        history[995] = NAN;
        history[996] = 0;
        history[997] = NAN;
        history[998] = 0;
        history[999] = NAN;
        history[1000] = 0;
        history[1001] = NAN;
        history[1002] = 0;
        history[1003] = NAN;
        history[1004] = 0;
        history[1005] = NAN;
        history[1006] = 0;
        history[1007] = NAN;
        history[1008] = 0;
        history[1009] = NAN;
        history[1010] = NAN;
        history[1011] = 0;
        history[1012] = NAN;
        history[1013] = 0;
        history[1014] = NAN;
        history[1015] = 0;
        history[1016] = NAN;
        history[1017] = NAN;
        history[1018] = 0;
        history[1019] = NAN;
        history[1020] = 0;
        history[1021] = NAN;
        history[1022] = 0;
        history[1023] = NAN;
        history[1024] = NAN;
        history[1025] = 0;
        history[1026] = NAN;
        history[1027] = 0;
        history[1028] = NAN;
        history[1029] = NAN;
        history[1030] = 0;
        history[1031] = NAN;
        history[1032] = NAN;
        history[1033] = 0;
        history[1034] = NAN;
        history[1035] = NAN;
        history[1036] = 0;
        history[1037] = NAN;
        history[1038] = 0;
        history[1039] = NAN;
        history[1040] = 0;
        history[1041] = NAN;
        history[1042] = 0;
        history[1043] = NAN;
        history[1044] = 0;
        history[1045] = NAN;
        history[1046] = 0;
        history[1047] = NAN;
        history[1048] = 0;
        history[1049] = NAN;
        history[1050] = 0;
        history[1051] = NAN;
        history[1052] = 0;
        history[1053] = NAN;
        history[1054] = 0;
        history[1055] = NAN;
        history[1056] = NAN;
        history[1057] = 0;
        history[1058] = NAN;
        history[1059] = 0;
        history[1060] = NAN;
        history[1061] = 0;
        history[1062] = NAN;
        history[1063] = 0;
        history[1064] = NAN;
        history[1065] = 0;
        history[1066] = NAN;
        history[1067] = 0;
        history[1068] = NAN;
        history[1069] = 0;
        history[1070] = NAN;
        history[1071] = 0;
        history[1072] = NAN;
        history[1073] = NAN;
        history[1074] = 0;
        history[1075] = NAN;
        history[1076] = 0;
        history[1077] = NAN;
        history[1078] = 0;
        history[1079] = NAN;
        history[1080] = 0;
        history[1081] = NAN;
        history[1082] = NAN;
        history[1083] = 0;
        history[1084] = NAN;
        history[1085] = 0;
        history[1086] = NAN;
        history[1087] = 0;
        history[1088] = NAN;
        history[1089] = 0;
        history[1090] = -INFINITY;
        history[1091] = 0;
        history[1092] = 0;
        history[1093] = 0;
        history[1094] = NAN;
        history[1095] = NAN;
        history[1096] = 0;
        history[1097] = NAN;
        history[1098] = 0;
        history[1099] = NAN;
        history[1100] = NAN;
        history[1101] = 0;
        history[1102] = NAN;
        history[1103] = 0;
        history[1104] = NAN;
        history[1105] = NAN;
        history[1106] = 0;
        history[1107] = NAN;
        history[1108] = NAN;
        history[1109] = 0;
        history[1110] = NAN;
        history[1111] = NAN;
        history[1112] = 0;
        history[1113] = NAN;
        history[1114] = 0;
        history[1115] = NAN;
        history[1116] = NAN;
        history[1117] = 0;
        history[1118] = NAN;
        history[1119] = 0;
        history[1120] = NAN;
        history[1121] = NAN;
        history[1122] = 0;
        history[1123] = NAN;
        history[1124] = 0;
        history[1125] = NAN;
        history[1126] = 0;
        history[1127] = NAN;
        history[1128] = 0;
        history[1129] = NAN;
        history[1130] = NAN;
        history[1131] = 0;
        history[1132] = NAN;
        history[1133] = 0;
        history[1134] = NAN;
        history[1135] = 0;
        history[1136] = NAN;
        history[1137] = 0;
        history[1138] = NAN;
        history[1139] = NAN;
        history[1140] = 0;
        history[1141] = NAN;
        history[1142] = 0;
        history[1143] = NAN;
        history[1144] = 0;
        history[1145] = NAN;
        history[1146] = 0;
        history[1147] = NAN;
        history[1148] = 0;
        history[1149] = NAN;
        history[1150] = NAN;
        history[1151] = 0;
        history[1152] = NAN;
        history[1153] = NAN;
        history[1154] = 0;
        history[1155] = NAN;
        history[1156] = 0;
        history[1157] = NAN;
        history[1158] = NAN;
        history[1159] = 0;
        history[1160] = NAN;
        history[1161] = 0;
        history[1162] = NAN;
        history[1163] = NAN;
        history[1164] = 0;
        history[1165] = NAN;
        history[1166] = 0;
        history[1167] = NAN;
        history[1168] = NAN;
        history[1169] = 0;
        history[1170] = NAN;
        history[1171] = NAN;
        history[1172] = 0;
        history[1173] = NAN;
        history[1174] = NAN;
        history[1175] = 0;
        history[1176] = NAN;
        history[1177] = 0;
        history[1178] = NAN;
        history[1179] = NAN;
        history[1180] = 0;
        history[1181] = NAN;
        history[1182] = 0;
        history[1183] = NAN;
        history[1184] = 0;
        history[1185] = NAN;
        history[1186] = NAN;
        history[1187] = 0;
        history[1188] = NAN;
        history[1189] = 0;
        history[1190] = NAN;
        history[1191] = NAN;
        history[1192] = 0;
        history[1193] = NAN;
        history[1194] = NAN;
        history[1195] = 0;
        history[1196] = NAN;
        history[1197] = NAN;
        history[1198] = 0;
        history[1199] = NAN;
        history[1200] = NAN;
        history[1201] = 0;
        history[1202] = NAN;
        history[1203] = 0;
        history[1204] = NAN;
        history[1205] = 0;
        history[1206] = NAN;
        history[1207] = 0;
        history[1208] = NAN;
        history[1209] = NAN;
        history[1210] = 0;
        history[1211] = NAN;
        history[1212] = 0;
        history[1213] = NAN;
        history[1214] = NAN;
        history[1215] = 0;
        history[1216] = NAN;
        history[1217] = NAN;
        history[1218] = 0;
        history[1219] = NAN;
        history[1220] = 0;
        history[1221] = NAN;
        history[1222] = NAN;
        history[1223] = 0;
        history[1224] = NAN;
        history[1225] = NAN;
        history[1226] = 0;
        history[1227] = NAN;
        history[1228] = 0;
        history[1229] = NAN;
        history[1230] = NAN;
        history[1231] = 0;
        history[1232] = NAN;
        history[1233] = NAN;
        history[1234] = 0;
        history[1235] = NAN;
        history[1236] = NAN;
        history[1237] = 0;
        history[1238] = NAN;
        history[1239] = 0;
        history[1240] = NAN;
        history[1241] = 0;
        history[1242] = NAN;
        history[1243] = 0;
        history[1244] = NAN;
        history[1245] = NAN;
        history[1246] = 0;
        history[1247] = NAN;
        history[1248] = 0;
        history[1249] = NAN;
        history[1250] = 0;
        history[1251] = NAN;
        history[1252] = 0;
        history[1253] = NAN;
        history[1254] = 0;
        history[1255] = NAN;
        history[1256] = 0;
        history[1257] = NAN;
        history[1258] = 0;
        history[1259] = NAN;
        history[1260] = NAN;
        history[1261] = 0;
        history[1262] = NAN;
        history[1263] = NAN;
        history[1264] = 0;
        history[1265] = NAN;
        history[1266] = 0;
        history[1267] = NAN;
        history[1268] = NAN;
        history[1269] = 0;
        history[1270] = NAN;
        history[1271] = 0;
        history[1272] = NAN;
        history[1273] = 0;
        history[1274] = NAN;
        history[1275] = 0;
        history[1276] = NAN;
        history[1277] = NAN;
        history[1278] = 0;
        history[1279] = NAN;
        history[1280] = 0;
        history[1281] = NAN;
        history[1282] = 0;
        history[1283] = NAN;
        history[1284] = NAN;
        history[1285] = 0;
        history[1286] = NAN;
        history[1287] = 0;
        history[1288] = NAN;
        history[1289] = 0;
        history[1290] = NAN;
        history[1291] = NAN;
        history[1292] = 0;
        history[1293] = NAN;
        history[1294] = 0;
        history[1295] = NAN;
        history[1296] = 0;
        history[1297] = NAN;
        history[1298] = 0;
        history[1299] = NAN;
        history[1300] = 0;
        history[1301] = -INFINITY;
        history[1302] = 0;
        history[1303] = NAN;
        history[1304] = 0;
        history[1305] = NAN;
        history[1306] = NAN;
        history[1307] = 0;
        history[1308] = NAN;
        history[1309] = 0;
        history[1310] = NAN;
        history[1311] = 0;
        history[1312] = NAN;
        history[1313] = NAN;
        history[1314] = 0;
        history[1315] = NAN;
        history[1316] = NAN;
        history[1317] = 0;
        history[1318] = NAN;
        history[1319] = 0;
        history[1320] = NAN;
        history[1321] = 0;
        history[1322] = NAN;
        history[1323] = 0;
        history[1324] = NAN;
        history[1325] = NAN;
        history[1326] = 0;
        history[1327] = NAN;
        history[1328] = 0;
        history[1329] = NAN;
        history[1330] = NAN;
        history[1331] = 0;
        history[1332] = NAN;
        history[1333] = NAN;
        history[1334] = 0;
        history[1335] = NAN;
        history[1336] = 0;
        history[1337] = NAN;
        history[1338] = NAN;
        history[1339] = 0;
        history[1340] = NAN;
        history[1341] = NAN;
        history[1342] = 0;
        history[1343] = NAN;
        history[1344] = 0;
        history[1345] = NAN;
        history[1346] = NAN;
        history[1347] = 0;
        history[1348] = NAN;
        history[1349] = NAN;
        history[1350] = 0;
        history[1351] = NAN;
        history[1352] = 0;
        history[1353] = NAN;
        history[1354] = NAN;
        history[1355] = 0;
        history[1356] = NAN;
        history[1357] = NAN;
        history[1358] = 0;
        history[1359] = NAN;
        history[1360] = 0;
        history[1361] = NAN;
        history[1362] = NAN;
        history[1363] = 0;
        history[1364] = NAN;
        history[1365] = NAN;
        history[1366] = 0;
        history[1367] = NAN;
        history[1368] = 0;
        history[1369] = NAN;
        history[1370] = NAN;
        history[1371] = 0;
        history[1372] = NAN;
        history[1373] = NAN;
        history[1374] = 0;
        history[1375] = NAN;
        history[1376] = NAN;
        history[1377] = 0;
        history[1378] = NAN;
        history[1379] = 0;
        history[1380] = NAN;
        history[1381] = 0;
        history[1382] = NAN;
        history[1383] = 0;
        history[1384] = NAN;
        history[1385] = 0;
        history[1386] = NAN;
        history[1387] = 0;
        history[1388] = NAN;
        history[1389] = NAN;
        history[1390] = 0;
        history[1391] = NAN;
        history[1392] = 0;
        history[1393] = NAN;
        history[1394] = 0;
        history[1395] = NAN;
        history[1396] = NAN;
        history[1397] = 0;
        history[1398] = NAN;
        history[1399] = NAN;
        history[1400] = 0;
        history[1401] = NAN;
        history[1402] = NAN;
        history[1403] = 0;
        history[1404] = NAN;
        history[1405] = 0;
        history[1406] = NAN;
        history[1407] = 0;
        history[1408] = NAN;
        history[1409] = NAN;
        history[1410] = 0;
        history[1411] = NAN;
        history[1412] = NAN;
        history[1413] = 0;
        history[1414] = NAN;
        history[1415] = 0;
        history[1416] = NAN;
        history[1417] = 0;
        history[1418] = NAN;
        history[1419] = 0;
        history[1420] = NAN;
        history[1421] = 0;
        history[1422] = NAN;
        history[1423] = 0;
        history[1424] = NAN;
        history[1425] = NAN;
        history[1426] = 0;
        history[1427] = NAN;
        history[1428] = 0;
        history[1429] = NAN;
        history[1430] = NAN;
        history[1431] = 0;
        history[1432] = NAN;
        history[1433] = 0;
        history[1434] = NAN;
        history[1435] = 0;
        history[1436] = NAN;
        history[1437] = 0;
        history[1438] = NAN;
        history[1439] = NAN;
        history[1440] = 0;
        history[1441] = NAN;
        history[1442] = NAN;
        history[1443] = 0;
        history[1444] = NAN;
        history[1445] = NAN;
        history[1446] = 0;
        history[1447] = NAN;
        history[1448] = 0;
        history[1449] = NAN;
        history[1450] = 0;
        history[1451] = NAN;
        history[1452] = NAN;
        history[1453] = 0;
        history[1454] = NAN;
        history[1455] = 0;
        history[1456] = NAN;
        history[1457] = 0;
        history[1458] = NAN;
        history[1459] = 0;
        history[1460] = NAN;
        history[1461] = 0;
        history[1462] = NAN;
        history[1463] = 0;
        history[1464] = NAN;
        history[1465] = 0;
        history[1466] = NAN;
        history[1467] = NAN;
        history[1468] = 0;
        history[1469] = NAN;
        history[1470] = 0;
        history[1471] = NAN;
        history[1472] = NAN;
        history[1473] = 0;
        history[1474] = NAN;
        history[1475] = 0;
        history[1476] = NAN;
        history[1477] = 0;
        history[1478] = NAN;
        history[1479] = 0;
        history[1480] = NAN;
        history[1481] = 0;
        history[1482] = 0;
        history[1483] = 0;
        history[1484] = 0;
        history[1485] = NAN;
        history[1486] = NAN;
        history[1487] = 0;
        history[1488] = NAN;
        history[1489] = 0;
        history[1490] = NAN;
        history[1491] = 0;
        history[1492] = NAN;
        history[1493] = 0;
        history[1494] = NAN;
        history[1495] = NAN;
        history[1496] = 0;
        history[1497] = NAN;
        history[1498] = 0;
        history[1499] = NAN;
        history[1500] = 0;
        history[1501] = NAN;
        history[1502] = NAN;
        history[1503] = 0;
        history[1504] = NAN;
        history[1505] = NAN;
        history[1506] = 0;
        history[1507] = NAN;
        history[1508] = NAN;
        history[1509] = 0;
        history[1510] = NAN;
        history[1511] = 0;
        history[1512] = NAN;
        history[1513] = NAN;
        history[1514] = 0;
        history[1515] = NAN;
        history[1516] = 0;
        history[1517] = NAN;
        history[1518] = NAN;
        history[1519] = 0;
        history[1520] = NAN;
        history[1521] = 0;
        history[1522] = NAN;
        history[1523] = NAN;
        history[1524] = 0;
        history[1525] = NAN;
        history[1526] = 0;
        history[1527] = NAN;
        history[1528] = 0;
        history[1529] = NAN;
        history[1530] = 0;
        history[1531] = NAN;
        history[1532] = 0;
        history[1533] = NAN;
        history[1534] = NAN;
        history[1535] = 0;
        history[1536] = NAN;
        history[1537] = 0;
        history[1538] = NAN;
        history[1539] = NAN;
        history[1540] = 0;
        history[1541] = NAN;
        history[1542] = 0;
        history[1543] = NAN;
        history[1544] = 0;
        history[1545] = NAN;
        history[1546] = NAN;
        history[1547] = 0;
        history[1548] = NAN;
        history[1549] = 0;
        history[1550] = NAN;
        history[1551] = 0;
        history[1552] = NAN;
        history[1553] = 0;
        history[1554] = NAN;
        history[1555] = 0;
        history[1556] = NAN;
        history[1557] = NAN;
        history[1558] = 0;
        history[1559] = NAN;
        history[1560] = NAN;
        history[1561] = 0;
        history[1562] = NAN;
        history[1563] = NAN;
        history[1564] = 0;
        history[1565] = NAN;
        history[1566] = 0;
        history[1567] = NAN;
        history[1568] = NAN;
        history[1569] = 0;
        history[1570] = NAN;
        history[1571] = 0;
        history[1572] = NAN;
        history[1573] = 0;
        history[1574] = NAN;
        history[1575] = 0;
        history[1576] = NAN;
        history[1577] = 0;
        history[1578] = NAN;
        history[1579] = 0;
        history[1580] = NAN;
        history[1581] = 0;
        history[1582] = NAN;
        history[1583] = NAN;
        history[1584] = 0;
        history[1585] = NAN;
        history[1586] = 0;
        history[1587] = NAN;
        history[1588] = 0;
        history[1589] = NAN;
        history[1590] = 0;
        history[1591] = NAN;
        history[1592] = 0;
        history[1593] = NAN;
        history[1594] = 0;
        history[1595] = NAN;
        history[1596] = 0;
        history[1597] = NAN;
        history[1598] = 0;
        history[1599] = NAN;
        history[1600] = 0;
        history[1601] = NAN;
        history[1602] = NAN;
        history[1603] = 0;
        history[1604] = NAN;
        history[1605] = NAN;
        history[1606] = 0;
        history[1607] = NAN;
        history[1608] = NAN;
        history[1609] = 0;
        history[1610] = NAN;
        history[1611] = 0;
        history[1612] = NAN;
        history[1613] = 0;
        history[1614] = NAN;
        history[1615] = 0;
        history[1616] = -INFINITY;
        history[1617] = 0;
        history[1618] = NAN;
        history[1619] = 0;
        history[1620] = NAN;
        history[1621] = NAN;
        history[1622] = 0;
        history[1623] = NAN;
        history[1624] = 0;
        history[1625] = NAN;
        history[1626] = 0;
        history[1627] = NAN;
        history[1628] = 0;
        history[1629] = NAN;
        history[1630] = 0;
        history[1631] = NAN;
        history[1632] = 0;
        history[1633] = NAN;
        history[1634] = 0;
        history[1635] = NAN;
        history[1636] = 0;
        history[1637] = NAN;
        history[1638] = NAN;
        history[1639] = 0;
        history[1640] = NAN;
        history[1641] = NAN;
        history[1642] = 0;
        history[1643] = NAN;
        history[1644] = NAN;
        history[1645] = 0;
        history[1646] = NAN;
        history[1647] = 0;
        history[1648] = NAN;
        history[1649] = 0;
        history[1650] = NAN;
        history[1651] = 0;
        history[1652] = NAN;
        history[1653] = 0;
        history[1654] = NAN;
        history[1655] = 0;
        history[1656] = NAN;
        history[1657] = NAN;
        history[1658] = 0;
        history[1659] = NAN;
        history[1660] = 0;
        history[1661] = NAN;
        history[1662] = NAN;
        history[1663] = 0;
        history[1664] = NAN;
        history[1665] = 0;
        history[1666] = NAN;
        history[1667] = NAN;
        history[1668] = 0;
        history[1669] = NAN;
        history[1670] = 0;
        history[1671] = NAN;
        history[1672] = 0;
        history[1673] = NAN;
        history[1674] = NAN;
        history[1675] = 0;
        history[1676] = NAN;
        history[1677] = 0;
        history[1678] = NAN;
        history[1679] = 0;
        history[1680] = NAN;
        history[1681] = 0;
        history[1682] = NAN;
        history[1683] = 0;
        history[1684] = 0;
        history[1685] = NAN;
        history[1686] = 0;
        history[1687] = NAN;
    } else if (lg == 2){
        history[1688] = 0;
        history[1689] = 0;
        history[1690] = 0;
        history[1691] = -INFINITY;
        history[1692] = 0;
        history[1693] = 0;
        history[1694] = INFINITY;
        history[1695] = 0;
        history[1696] = 0;
        history[1697] = INFINITY;
        history[1698] = 0;
        history[1699] = INFINITY;
        history[1700] = 0;
        history[1701] = -INFINITY;
        history[1702] = 0;
        history[1703] = INFINITY;
        history[1704] = -INFINITY;
        history[1705] = 0;
        history[1706] = 0;
        history[1707] = 0;
        history[1708] = 0;
        history[1709] = 0;
        history[1710] = 0;
        history[1711] = 0;
        history[1712] = 0;
        history[1713] = 0;
        history[1714] = 0;
        history[1715] = 0;
        history[1716] = 0;
        history[1717] = NAN;
        history[1718] = 0;
        history[1719] = NAN;
        history[1720] = 0;
        history[1721] = -INFINITY;
        history[1722] = 0;
        history[1723] = NAN;
        history[1724] = 0;
        history[1725] = NAN;
        history[1726] = 0;
        history[1727] = NAN;
        history[1728] = 0;
        history[1729] = NAN;
        history[1730] = 0;
        history[1731] = NAN;
        history[1732] = 0;
        history[1733] = NAN;
        history[1734] = 0;
        history[1735] = NAN;
        history[1736] = 0;
        history[1737] = NAN;
        history[1738] = 0;
        history[1739] = NAN;
        history[1740] = 0;
        history[1741] = NAN;
        history[1742] = 0;
        history[1743] = NAN;
        history[1744] = 0;
        history[1745] = NAN;
        history[1746] = 0;
        history[1747] = NAN;
        history[1748] = 0;
        history[1749] = NAN;
        history[1750] = 0;
        history[1751] = NAN;
        history[1752] = 0;
        history[1753] = NAN;
        history[1754] = 0;
        history[1755] = NAN;
        history[1756] = 0;
        history[1757] = NAN;
        history[1758] = 0;
        history[1759] = NAN;
        history[1760] = 0;
        history[1761] = NAN;
        history[1762] = 0;
        history[1763] = NAN;
        history[1764] = 0;
        history[1765] = NAN;
        history[1766] = 0;
        history[1767] = NAN;
        history[1768] = 0;
        history[1769] = NAN;
        history[1770] = 0;
        history[1771] = NAN;
        history[1772] = 0;
        history[1773] = NAN;
        history[1774] = 0;
        history[1775] = NAN;
        history[1776] = 0;
        history[1777] = NAN;
        history[1778] = 0;
        history[1779] = NAN;
        history[1780] = 0;
        history[1781] = NAN;
        history[1782] = 0;
        history[1783] = NAN;
        history[1784] = 0;
        history[1785] = NAN;
        history[1786] = 0;
        history[1787] = NAN;
        history[1788] = 0;
        history[1789] = NAN;
    }
    if (lg == 0){
        history[1790] = 0;
        history[1791] = NAN;
        history[1792] = 0;
        history[1793] = NAN;
        history[1794] = 0;
        history[1795] = NAN;
        history[1796] = 0;
        history[1797] = -INFINITY;
        history[1798] = 0;
        history[1799] = 0;
        history[1800] = 0;
        history[1801] = 0;
        history[1802] = 0;
        history[1803] = 0;
        history[1804] = 0;
        history[1805] = INFINITY;
        history[1806] = 0;
        history[1807] = -INFINITY;
        history[1808] = 0;
        history[1809] = -INFINITY;
        history[1810] = 0;
        history[1811] = 0;
        history[1812] = 0;
        history[1813] = -INFINITY;
        history[1814] = 0;
        history[1815] = 0;
        history[1816] = 0;
        history[1817] = 0;
        history[1818] = 0;
        history[1819] = 0;
        history[1820] = -INFINITY;
        history[1821] = 0;
        history[1822] = INFINITY;
        history[1823] = 0;
        history[1824] = INFINITY;
        history[1825] = 0;
        history[1826] = INFINITY;
        history[1827] = 0;
        history[1828] = INFINITY;
        history[1829] = 0;
        history[1830] = -INFINITY;
        history[1831] = 0;
        history[1832] = -INFINITY;
        history[1833] = 0;
        history[1834] = 0;
        history[1835] = 0;
        history[1836] = 0;
        history[1837] = -INFINITY;
        history[1838] = 0;
        history[1839] = -INFINITY;
        history[1840] = 0;
        history[1841] = 0;
        history[1842] = 0;
        history[1843] = 0;
        history[1844] = 0;
        history[1845] = 0;
        history[1846] = 0;
        history[1847] = INFINITY;
        history[1848] = 0;
        history[1849] = 0;
        history[1850] = 0;
        history[1851] = 0;
        history[1852] = 0;
        history[1853] = 0;
        history[1854] = 0;
        history[1855] = 0;
        history[1856] = 0;
        history[1857] = 0;
        history[1858] = 0;
        history[1859] = 0;
        history[1860] = 0;
        history[1861] = 0;
        history[1862] = 0;
        history[1863] = 0;
        history[1864] = 0;
        history[1865] = 0;
        history[1866] = 0;
        history[1867] = 0;
        history[1868] = 0;
        history[1869] = 0;
        history[1870] = -INFINITY;
        history[1871] = 0;
        history[1872] = 0;
        history[1873] = 0;
        history[1874] = INFINITY;
        history[1875] = 0;
        history[1876] = INFINITY;
        history[1877] = 0;
        history[1878] = INFINITY;
        history[1879] = 0;
        history[1880] = 0;
        history[1881] = 0;
        history[1882] = 0;
        history[1883] = -INFINITY;
        history[1884] = 0;
        history[1885] = -INFINITY;
        history[1886] = 0;
        history[1887] = 0;
        history[1888] = 0;
        history[1889] = 0;
        history[1890] = 0;
        history[1891] = 0;
        history[1892] = 0;
        history[1893] = 0;
        history[1894] = 0;
        history[1895] = 0;
        history[1896] = 0;
        history[1897] = 0;
        history[1898] = 0;
        history[1899] = 0;
        history[1900] = 0;
        history[1901] = 0;
        history[1902] = 0;
        history[1903] = 0;
        history[1904] = 0;
        history[1905] = 0;
        history[1906] = 0;
        history[1907] = 0;
        history[1908] = INFINITY;
        history[1909] = 0;
        history[1910] = 0;
        history[1911] = 0;
        history[1912] = NAN;
        history[1913] = 0;
        history[1914] = NAN;
        history[1915] = 0;
        history[1916] = NAN;
        history[1917] = 0;
        history[1918] = NAN;
        history[1919] = 0;
        history[1920] = NAN;
        history[1921] = 0;
        history[1922] = NAN;
        history[1923] = 0;
        history[1924] = NAN;
        history[1925] = 0;
        history[1926] = NAN;
        history[1927] = 0;
        history[1928] = -INFINITY;
        history[1929] = 0;
        history[1930] = INFINITY;
        history[1931] = 0;
        history[1932] = 0;
        history[1933] = 0;
        history[1934] = -INFINITY;
        history[1935] = 0;
        history[1936] = -INFINITY;
        history[1937] = 0;
        history[1938] = -INFINITY;
        history[1939] = 0;
        history[1940] = 0;
        history[1941] = 0;
        history[1942] = INFINITY;
        history[1943] = 0;
        history[1944] = INFINITY;
        history[1945] = 0;
        history[1946] = 0;
        history[1947] = 0;
        history[1948] = 0;
        history[1949] = 0;
        history[1950] = 0;
        history[1951] = 0;
        history[1952] = 0;
        history[1953] = 0;
        history[1954] = 0;
        history[1955] = 0;
        history[1956] = 0;
        history[1957] = 0;
        history[1958] = 0;
        history[1959] = 0;
        history[1960] = 0;
        history[1961] = INFINITY;
        history[1962] = 0;
        history[1963] = 0;
        history[1964] = 0;
        history[1965] = 0;
        history[1966] = 0;
        history[1967] = 0;
        history[1968] = 0;
        history[1969] = NAN;
        history[1970] = 0;
        history[1971] = NAN;
        history[1972] = 0;
        history[1973] = NAN;
        history[1974] = 0;
        history[1975] = NAN;
        history[1976] = 0;
        history[1977] = NAN;
        history[1978] = 0;
        history[1979] = NAN;
        history[1980] = 0;
        history[1981] = NAN;
        history[1982] = 0;
        history[1983] = NAN;
        history[1984] = 0;
        history[1985] = NAN;
        history[1986] = 0;
        history[1987] = NAN;
        history[1988] = 0;
        history[1989] = NAN;
        history[1990] = 0;
        history[1991] = NAN;
        history[1992] = 0;
        history[1993] = NAN;
        history[1994] = 0;
        history[1995] = NAN;
        history[1996] = 0;
        history[1997] = NAN;
        history[1998] = 0;
        history[1999] = NAN;
        history[2000] = 0;
        history[2001] = NAN;
        history[2002] = 0;
        history[2003] = NAN;
        history[2004] = 0;
        history[2005] = NAN;
        history[2006] = 0;
        history[2007] = NAN;
        history[2008] = 0;
        history[2009] = NAN;
        history[2010] = 0;
        history[2011] = NAN;
        history[2012] = 0;
        history[2013] = NAN;
        history[2014] = 0;
        history[2015] = NAN;
        history[2016] = 0;
        history[2017] = NAN;
        history[2018] = 0;
        history[2019] = NAN;
        history[2020] = 0;
        history[2021] = NAN;
        history[2022] = 0;
        history[2023] = NAN;
        history[2024] = 0;
        history[2025] = NAN;
        history[2026] = 0;
        history[2027] = NAN;
        history[2028] = 0;
        history[2029] = -INFINITY;
        history[2030] = 0;
        history[2031] = -INFINITY;
        history[2032] = 0;
        history[2033] = 0;
        history[2034] = 0;
        history[2035] = INFINITY;
        history[2036] = 0;
        history[2037] = -INFINITY;
        history[2038] = 0;
        history[2039] = 0;
        history[2040] = 0;
        history[2041] = 0;
        history[2042] = 0;
        history[2043] = INFINITY;
        history[2044] = 0;
        history[2045] = INFINITY;
        history[2046] = 0;
        history[2047] = 0;
        history[2048] = 0;
        history[2049] = 0;
        history[2050] = INFINITY;
        history[2051] = 0;
        history[2052] = INFINITY;
        history[2053] = 0;
        history[2054] = 0;
        history[2055] = 0;
        history[2056] = 0;
        history[2057] = 0;
        history[2058] = 0;
        history[2059] = 0;
        history[2060] = 0;
        history[2061] = 0;
        history[2062] = 0;
        history[2063] = 0;
        history[2064] = 0;
        history[2065] = 0;
        history[2066] = 0;
        history[2067] = 0;
        history[2068] = NAN;
        history[2069] = 0;
        history[2070] = NAN;
        history[2071] = 0;
        history[2072] = NAN;
        history[2073] = 0;
        history[2074] = NAN;
        history[2075] = 0;
        history[2076] = NAN;
        history[2077] = 0;
        history[2078] = NAN;
        history[2079] = 0;
        history[2080] = NAN;
        history[2081] = 0;
        history[2082] = NAN;
        history[2083] = 0;
        history[2084] = NAN;
        history[2085] = 0;
        history[2086] = NAN;
        history[2087] = 0;
        history[2088] = NAN;
        history[2089] = 0;
        history[2090] = NAN;
        history[2091] = 0;
        history[2092] = NAN;
        history[2093] = 0;
        history[2094] = -INFINITY;
        history[2095] = 0;
        history[2096] = -INFINITY;
        history[2097] = 0;
        history[2098] = INFINITY;
        history[2099] = 0;
        history[2100] = INFINITY;
        history[2101] = 0;
        history[2102] = INFINITY;
        history[2103] = 0;
        history[2104] = INFINITY;
        history[2105] = 0;
        history[2106] = INFINITY;
        history[2107] = 0;
        history[2108] = INFINITY;
        history[2109] = 0;
        history[2110] = INFINITY;
        history[2111] = 0;
        history[2112] = 0;
        history[2113] = 0;
        history[2114] = 0;
        history[2115] = 0;
        history[2116] = 0;
        history[2117] = 0;
        history[2118] = 0;
        history[2119] = 0;
        history[2120] = 0;
        history[2121] = 0;
        history[2122] = 0;
        history[2123] = 0;
        history[2124] = -INFINITY;
        history[2125] = 0;
        history[2126] = INFINITY;
        history[2127] = 0;
        history[2128] = INFINITY;
        history[2129] = 0;
        history[2130] = 0;
        history[2131] = 0;
        history[2132] = 0;
        history[2133] = 0;
        history[2134] = 0;
        history[2135] = 0;
        history[2136] = 0;
        history[2137] = 0;
        history[2138] = 0;
        history[2139] = -INFINITY;
        history[2140] = 0;
        history[2141] = -INFINITY;
        history[2142] = 0;
        history[2143] = INFINITY;
        history[2144] = 0;
        history[2145] = -INFINITY;
        history[2146] = 0;
        history[2147] = -INFINITY;
        history[2148] = 0;
        history[2149] = 0;
        history[2150] = 0;
        history[2151] = 0;
        history[2152] = 0;
        history[2153] = 0;
        history[2154] = 0;
        history[2155] = 0;
        history[2156] = 0;
        history[2157] = 0;
        history[2158] = 0;
        history[2159] = 0;
        history[2160] = 0;
        history[2161] = 0;
        history[2162] = 0;
        history[2163] = 0;
        history[2164] = 0;
        history[2165] = 0;
        history[2166] = 0;
        history[2167] = 0;
        history[2168] = 0;
        history[2169] = 0;
        history[2170] = 0;
        history[2171] = INFINITY;
        history[2172] = 0;
        history[2173] = 0;
        history[2174] = 0;
        history[2175] = 0;
        history[2176] = 0;
        history[2177] = 0;
        history[2178] = 0;
        history[2179] = 0;
        history[2180] = 0;
        history[2181] = NAN;
        history[2182] = 0;
        history[2183] = NAN;
        history[2184] = 0;
        history[2185] = NAN;
        history[2186] = 0;
        history[2187] = NAN;
        history[2188] = 0;
        history[2189] = NAN;
        history[2190] = 0;
        history[2191] = NAN;
        history[2192] = 0;
        history[2193] = NAN;
        history[2194] = 0;
        history[2195] = NAN;
        history[2196] = 0;
        history[2197] = NAN;
        history[2198] = 0;
        history[2199] = NAN;
        history[2200] = 0;
        history[2201] = -INFINITY;
        history[2202] = 0;
        history[2203] = 0;
        history[2204] = 0;
        history[2205] = 0;
        history[2206] = 0;
        history[2207] = 0;
        history[2208] = -INFINITY;
        history[2209] = 0;
        history[2210] = -INFINITY;
        history[2211] = 0;
        history[2212] = -INFINITY;
        history[2213] = 0;
        history[2214] = -INFINITY;
        history[2215] = 0;
        history[2216] = 0;
        history[2217] = 0;
        history[2218] = INFINITY;
        history[2219] = 0;
        history[2220] = INFINITY;
        history[2221] = 0;
        history[2222] = INFINITY;
        history[2223] = 0;
        history[2224] = INFINITY;
        history[2225] = 0;
        history[2226] = 0;
        history[2227] = 0;
        history[2228] = 0;
        history[2229] = 0;
        history[2230] = 0;
        history[2231] = 0;
        history[2232] = 0;
        history[2233] = 0;
        history[2234] = 0;
        history[2235] = 0;
        history[2236] = 0;
        history[2237] = 0;
        history[2238] = 0;
        history[2239] = 0;
        history[2240] = 0;
        history[2241] = 0;
        history[2242] = 0;
        history[2243] = 0;
        history[2244] = 0;
        history[2245] = INFINITY;
        history[2246] = 0;
        history[2247] = 0;
        history[2248] = 0;
        history[2249] = 0;
        history[2250] = NAN;
    } else if (lg == 1){
        history[2251] = 0;
        history[2252] = NAN;
        history[2253] = 0;
        history[2254] = NAN;
        history[2255] = 0;
        history[2256] = NAN;
        history[2257] = 0;
        history[2258] = NAN;
        history[2259] = 0;
        history[2260] = NAN;
        history[2261] = 0;
        history[2262] = NAN;
        history[2263] = 0;
        history[2264] = NAN;
        history[2265] = 0;
        history[2266] = NAN;
        history[2267] = 0;
        history[2268] = NAN;
        history[2269] = 0;
        history[2270] = NAN;
        history[2271] = 0;
        history[2272] = NAN;
        history[2273] = 0;
        history[2274] = NAN;
        history[2275] = 0;
        history[2276] = NAN;
        history[2277] = 0;
        history[2278] = NAN;
        history[2279] = 0;
        history[2280] = NAN;
        history[2281] = 0;
        history[2282] = -INFINITY;
        history[2283] = 0;
        history[2284] = 0;
        history[2285] = 0;
        history[2286] = 0;
        history[2287] = -INFINITY;
        history[2288] = 0;
        history[2289] = INFINITY;
        history[2290] = 0;
        history[2291] = 0;
        history[2292] = 0;
        history[2293] = INFINITY;
        history[2294] = 0;
        history[2295] = INFINITY;
        history[2296] = 0;
        history[2297] = 0;
        history[2298] = 0;
        history[2299] = 0;
        history[2300] = 0;
        history[2301] = 0;
        history[2302] = -INFINITY;
        history[2303] = 0;
        history[2304] = -INFINITY;
        history[2305] = 0;
        history[2306] = 0;
        history[2307] = 0;
        history[2308] = 0;
        history[2309] = 0;
        history[2310] = 0;
        history[2311] = -INFINITY;
        history[2312] = 0;
        history[2313] = -INFINITY;
        history[2314] = 0;
        history[2315] = 0;
        history[2316] = 0;
        history[2317] = 0;
        history[2318] = 0;
        history[2319] = INFINITY;
        history[2320] = 0;
        history[2321] = INFINITY;
        history[2322] = 0;
        history[2323] = INFINITY;
        history[2324] = 0;
        history[2325] = INFINITY;
        history[2326] = 0;
        history[2327] = INFINITY;
        history[2328] = 0;
        history[2329] = 0;
        history[2330] = 0;
        history[2331] = 0;
        history[2332] = INFINITY;
        history[2333] = 0;
        history[2334] = INFINITY;
        history[2335] = 0;
        history[2336] = INFINITY;
        history[2337] = 0;
        history[2338] = 0;
        history[2339] = 0;
        history[2340] = -INFINITY;
        history[2341] = 0;
        history[2342] = -INFINITY;
        history[2343] = 0;
        history[2344] = -INFINITY;
        history[2345] = 0;
        history[2346] = 0;
        history[2347] = 0;
        history[2348] = 0;
        history[2349] = 0;
        history[2350] = 0;
        history[2351] = 0;
        history[2352] = 0;
        history[2353] = 0;
        history[2354] = 0;
        history[2355] = 0;
        history[2356] = -INFINITY;
        history[2357] = 0;
        history[2358] = -INFINITY;
        history[2359] = 0;
        history[2360] = 0;
        history[2361] = 0;
        history[2362] = INFINITY;
        history[2363] = 0;
        history[2364] = INFINITY;
        history[2365] = 0;
        history[2366] = 0;
        history[2367] = 0;
        history[2368] = 0;
        history[2369] = 0;
        history[2370] = 0;
        history[2371] = 0;
        history[2372] = 0;
        history[2373] = 0;
        history[2374] = 0;
        history[2375] = 0;
        history[2376] = 0;
        history[2377] = 0;
        history[2378] = 0;
        history[2379] = 0;
        history[2380] = 0;
        history[2381] = 0;
        history[2382] = 0;
        history[2383] = 0;
        history[2384] = 0;
        history[2385] = 0;
        history[2386] = 0;
        history[2387] = NAN;
        history[2388] = 0;
        history[2389] = NAN;
        history[2390] = 0;
        history[2391] = NAN;
        history[2392] = 0;
        history[2393] = NAN;
        history[2394] = 0;
        history[2395] = NAN;
        history[2396] = 0;
        history[2397] = NAN;
        history[2398] = 0;
        history[2399] = NAN;
        history[2400] = 0;
        history[2401] = NAN;
        history[2402] = 0;
        history[2403] = NAN;
        history[2404] = 0;
        history[2405] = NAN;
        history[2406] = 0;
        history[2407] = NAN;
        history[2408] = 0;
        history[2409] = NAN;
        history[2410] = 0;
        history[2411] = NAN;
        history[2412] = 0;
        history[2413] = NAN;
        history[2414] = 0;
        history[2415] = NAN;
        history[2416] = 0;
        history[2417] = NAN;
        history[2418] = 0;
        history[2419] = NAN;
        history[2420] = 0;
        history[2421] = -INFINITY;
        history[2422] = 0;
        history[2423] = 0;
        history[2424] = 0;
        history[2425] = 0;
        history[2426] = 0;
        history[2427] = 0;
        history[2428] = 0;
        history[2429] = -INFINITY;
        history[2430] = 0;
        history[2431] = 0;
        history[2432] = 0;
        history[2433] = 0;
        history[2434] = 0;
        history[2435] = 0;
        history[2436] = 0;
        history[2437] = 0;
        history[2438] = 0;
        history[2439] = -INFINITY;
        history[2440] = 0;
        history[2441] = 0;
        history[2442] = 0;
        history[2443] = 0;
        history[2444] = 0;
        history[2445] = 0;
        history[2446] = -INFINITY;
        history[2447] = 0;
        history[2448] = INFINITY;
        history[2449] = 0;
        history[2450] = INFINITY;
        history[2451] = 0;
        history[2452] = 0;
        history[2453] = 0;
        history[2454] = -INFINITY;
        history[2455] = 0;
        history[2456] = -INFINITY;
        history[2457] = 0;
        history[2458] = 0;
        history[2459] = 0;
        history[2460] = 0;
        history[2461] = 0;
        history[2462] = 0;
        history[2463] = 0;
        history[2464] = 0;
        history[2465] = 0;
        history[2466] = 0;
        history[2467] = -INFINITY;
        history[2468] = 0;
        history[2469] = 0;
        history[2470] = 0;
        history[2471] = 0;
        history[2472] = 0;
        history[2473] = 0;
        history[2474] = 0;
        history[2475] = 0;
        history[2476] = 0;
        history[2477] = 0;
        history[2478] = 0;
        history[2479] = NAN;
        history[2480] = 0;
        history[2481] = NAN;
        history[2482] = 0;
        history[2483] = NAN;
        history[2484] = 0;
        history[2485] = NAN;
        history[2486] = 0;
        history[2487] = NAN;
        history[2488] = 0;
        history[2489] = NAN;
        history[2490] = 0;
        history[2491] = NAN;
        history[2492] = 0;
        history[2493] = NAN;
        history[2494] = 0;
        history[2495] = NAN;
        history[2496] = 0;
        history[2497] = NAN;
        history[2498] = 0;
        history[2499] = NAN;
        history[2500] = 0;
        history[2501] = NAN;
        history[2502] = 0;
        history[2503] = NAN;
        history[2504] = 0;
        history[2505] = NAN;
        history[2506] = 0;
        history[2507] = NAN;
        history[2508] = 0;
        history[2509] = NAN;
        history[2510] = 0;
        history[2511] = NAN;
        history[2512] = 0;
        history[2513] = NAN;
        history[2514] = 0;
        history[2515] = NAN;
        history[2516] = 0;
        history[2517] = NAN;
        history[2518] = 0;
        history[2519] = NAN;
        history[2520] = 0;
        history[2521] = NAN;
        history[2522] = 0;
        history[2523] = NAN;
        history[2524] = NAN;
        history[2525] = 0;
        history[2526] = NAN;
        history[2527] = 0;
        history[2528] = NAN;
        history[2529] = 0;
        history[2530] = NAN;
        history[2531] = 0;
        history[2532] = NAN;
        history[2533] = 0;
        history[2534] = NAN;
        history[2535] = 0;
        history[2536] = NAN;
        history[2537] = 0;
        history[2538] = NAN;
        history[2539] = 0;
        history[2540] = NAN;
        history[2541] = 0;
        history[2542] = NAN;
        history[2543] = 0;
        history[2544] = NAN;
        history[2545] = 0;
        history[2546] = NAN;
        history[2547] = 0;
        history[2548] = NAN;
        history[2549] = 0;
        history[2550] = NAN;
        history[2551] = 0;
        history[2552] = NAN;
        history[2553] = 0;
        history[2554] = NAN;
        history[2555] = 0;
        history[2556] = NAN;
        history[2557] = 0;
        history[2558] = NAN;
        history[2559] = 0;
        history[2560] = NAN;
        history[2561] = 0;
        history[2562] = NAN;
        history[2563] = 0;
        history[2564] = NAN;
        history[2565] = 0;
        history[2566] = NAN;
        history[2567] = 0;
        history[2568] = NAN;
        history[2569] = 0;
        history[2570] = NAN;
        history[2571] = 0;
        history[2572] = -INFINITY;
        history[2573] = 0;
        history[2574] = 0;
        history[2575] = 0;
        history[2576] = -INFINITY;
        history[2577] = 0;
        history[2578] = 0;
        history[2579] = 0;
        history[2580] = -INFINITY;
        history[2581] = 0;
        history[2582] = -INFINITY;
        history[2583] = 0;
        history[2584] = -INFINITY;
        history[2585] = 0;
        history[2586] = -INFINITY;
        history[2587] = 0;
        history[2588] = 0;
        history[2589] = 0;
        history[2590] = 0;
        history[2591] = 0;
        history[2592] = 0;
        history[2593] = 0;
        history[2594] = 0;
        history[2595] = 0;
        history[2596] = 0;
        history[2597] = 0;
        history[2598] = 0;
        history[2599] = 0;
        history[2600] = 0;
        history[2601] = 0;
        history[2602] = 0;
        history[2603] = 0;
        history[2604] = 0;
        history[2605] = 0;
        history[2606] = 0;
        history[2607] = 0;
        history[2608] = 0;
        history[2609] = 0;
        history[2610] = 0;
        history[2611] = 0;
        history[2612] = 0;
        history[2613] = 0;
        history[2614] = -INFINITY;
        history[2615] = 0;
        history[2616] = 0;
        history[2617] = 0;
        history[2618] = 0;
        history[2619] = 0;
        history[2620] = 0;
        history[2621] = 0;
        history[2622] = -INFINITY;
        history[2623] = 0;
        history[2624] = -INFINITY;
        history[2625] = 0;
        history[2626] = -INFINITY;
        history[2627] = 0;
        history[2628] = -INFINITY;
        history[2629] = 0;
        history[2630] = -INFINITY;
        history[2631] = 0;
        history[2632] = INFINITY;
        history[2633] = 0;
        history[2634] = INFINITY;
        history[2635] = 0;
        history[2636] = -INFINITY;
        history[2637] = 0;
        history[2638] = -INFINITY;
        history[2639] = 0;
        history[2640] = 0;
        history[2641] = 0;
        history[2642] = INFINITY;
        history[2643] = 0;
        history[2644] = INFINITY;
        history[2645] = 0;
        history[2646] = 0;
        history[2647] = 0;
        history[2648] = 0;
        history[2649] = -INFINITY;
        history[2650] = 0;
        history[2651] = -INFINITY;
        history[2652] = 0;
        history[2653] = -INFINITY;
        history[2654] = 0;
        history[2655] = 0;
        history[2656] = 0;
        history[2657] = 0;
        history[2658] = 0;
        history[2659] = 0;
        history[2660] = 0;
        history[2661] = INFINITY;
        history[2662] = 0;
        history[2663] = 0;
        history[2664] = 0;
        history[2665] = 0;
        history[2666] = 0;
        history[2667] = 0;
        history[2668] = 0;
        history[2669] = 0;
        history[2670] = 0;
        history[2671] = 0;
        history[2672] = 0;
        history[2673] = 0;
        history[2674] = 0;
        history[2675] = 0;
        history[2676] = 0;
        history[2677] = -INFINITY;
        history[2678] = 0;
        history[2679] = -INFINITY;
        history[2680] = 0;
        history[2681] = -INFINITY;
        history[2682] = 0;
        history[2683] = 0;
        history[2684] = 0;
        history[2685] = 0;
        history[2686] = 0;
        history[2687] = 0;
        history[2688] = 0;
        history[2689] = 0;
        history[2690] = 0;
        history[2691] = NAN;
        history[2692] = 0;
        history[2693] = NAN;
        history[2694] = 0;
        history[2695] = NAN;
        history[2696] = 0;
        history[2697] = NAN;
        history[2698] = 0;
        history[2699] = NAN;
        history[2700] = 0;
        history[2701] = NAN;
        history[2702] = 0;
        history[2703] = NAN;
        history[2704] = 0;
        history[2705] = NAN;
        history[2706] = 0;
        history[2707] = NAN;
        history[2708] = 0;
        history[2709] = NAN;
        history[2710] = 0;
        history[2711] = NAN;
        history[2712] = 0;
        history[2713] = NAN;
        history[2714] = 0;
        history[2715] = NAN;
        history[2716] = 0;
        history[2717] = NAN;
        history[2718] = 0;
        history[2719] = NAN;
        history[2720] = 0;
        history[2721] = NAN;
        history[2722] = 0;
        history[2723] = NAN;
        history[2724] = 0;
        history[2725] = NAN;
        history[2726] = 0;
        history[2727] = NAN;
        history[2728] = 0;
        history[2729] = NAN;
        history[2730] = 0;
        history[2731] = NAN;
        history[2732] = 0;
        history[2733] = NAN;
        history[2734] = 0;
        history[2735] = NAN;
        history[2736] = 0;
        history[2737] = NAN;
        history[2738] = 0;
        history[2739] = NAN;
        history[2740] = 0;
        history[2741] = NAN;
        history[2742] = 0;
        history[2743] = NAN;
        history[2744] = 0;
        history[2745] = -INFINITY;
        history[2746] = 0;
        history[2747] = 0;
        history[2748] = 0;
        history[2749] = -INFINITY;
        history[2750] = 0;
        history[2751] = 0;
        history[2752] = 0;
        history[2753] = 0;
        history[2754] = 0;
        history[2755] = 0;
        history[2756] = 0;
        history[2757] = 0;
        history[2758] = 0;
        history[2759] = 0;
        history[2760] = -INFINITY;
        history[2761] = 0;
        history[2762] = 0;
        history[2763] = 0;
        history[2764] = 0;
        history[2765] = 0;
        history[2766] = -INFINITY;
        history[2767] = 0;
        history[2768] = -INFINITY;
        history[2769] = 0;
        history[2770] = INFINITY;
        history[2771] = 0;
        history[2772] = 0;
        history[2773] = 0;
        history[2774] = 0;
        history[2775] = 0;
        history[2776] = 0;
        history[2777] = 0;
        history[2778] = NAN;
        history[2779] = 0;
        history[2780] = NAN;
        history[2781] = 0;
        history[2782] = NAN;
        history[2783] = 0;
        history[2784] = NAN;
        history[2785] = 0;
        history[2786] = NAN;
        history[2787] = 0;
        history[2788] = NAN;
        history[2789] = NAN;
        history[2790] = 0;
        history[2791] = NAN;
        history[2792] = 0;
        history[2793] = NAN;
        history[2794] = 0;
        history[2795] = NAN;
        history[2796] = 0;
        history[2797] = NAN;
        history[2798] = 0;
        history[2799] = NAN;
        history[2800] = 0;
        history[2801] = NAN;
        history[2802] = 0;
        history[2803] = NAN;
        history[2804] = 0;
        history[2805] = NAN;
        history[2806] = 0;
        history[2807] = NAN;
        history[2808] = 0;
        history[2809] = NAN;
        history[2810] = 0;
        history[2811] = NAN;
        history[2812] = 0;
        history[2813] = -INFINITY;
        history[2814] = 0;
        history[2815] = INFINITY;
        history[2816] = 0;
        history[2817] = -INFINITY;
        history[2818] = 0;
        history[2819] = -INFINITY;
        history[2820] = 0;
        history[2821] = -INFINITY;
        history[2822] = 0;
        history[2823] = -INFINITY;
        history[2824] = 0;
        history[2825] = -INFINITY;
        history[2826] = 0;
        history[2827] = 0;
        history[2828] = 0;
        history[2829] = 0;
        history[2830] = 0;
        history[2831] = 0;
        history[2832] = 0;
        history[2833] = 0;
        history[2834] = 0;
        history[2835] = 0;
        history[2836] = 0;
        history[2837] = 0;
        history[2838] = -INFINITY;
        history[2839] = 0;
        history[2840] = -INFINITY;
        history[2841] = 0;
        history[2842] = -INFINITY;
        history[2843] = 0;
        history[2844] = 0;
        history[2845] = 0;
        history[2846] = -INFINITY;
        history[2847] = 0;
        history[2848] = 0;
        history[2849] = 0;
        history[2850] = INFINITY;
        history[2851] = 0;
        history[2852] = 0;
        history[2853] = 0;
        history[2854] = 0;
        history[2855] = 0;
        history[2856] = 0;
        history[2857] = -INFINITY;
        history[2858] = 0;
        history[2859] = 0;
        history[2860] = 0;
        history[2861] = -INFINITY;
        history[2862] = 0;
        history[2863] = -INFINITY;
        history[2864] = 0;
        history[2865] = 0;
        history[2866] = 0;
        history[2867] = 0;
        history[2868] = 0;
        history[2869] = INFINITY;
        history[2870] = 0;
        history[2871] = 0;
        history[2872] = 0;
        history[2873] = NAN;
        history[2874] = 0;
        history[2875] = NAN;
        history[2876] = 0;
        history[2877] = NAN;
        history[2878] = 0;
        history[2879] = NAN;
        history[2880] = 0;
        history[2881] = NAN;
        history[2882] = 0;
        history[2883] = NAN;
        history[2884] = 0;
        history[2885] = NAN;
        history[2886] = 0;
        history[2887] = NAN;
        history[2888] = 0;
        history[2889] = NAN;
        history[2890] = 0;
        history[2891] = NAN;
        history[2892] = 0;
        history[2893] = NAN;
        history[2894] = 0;
        history[2895] = NAN;
        history[2896] = 0;
        history[2897] = NAN;
        history[2898] = 0;
        history[2899] = -INFINITY;
        history[2900] = 0;
        history[2901] = 0;
        history[2902] = 0;
        history[2903] = 0;
        history[2904] = 0;
        history[2905] = 0;
        history[2906] = 0;
        history[2907] = 0;
        history[2908] = 0;
        history[2909] = 0;
        history[2910] = 0;
        history[2911] = 0;
        history[2912] = 0;
        history[2913] = 0;
        history[2914] = 0;
        history[2915] = 0;
        history[2916] = 0;
        history[2917] = 0;
        history[2918] = 0;
        history[2919] = 0;
        history[2920] = 0;
        history[2921] = 0;
        history[2922] = 0;
        history[2923] = 0;
        history[2924] = 0;
        history[2925] = 0;
        history[2926] = INFINITY;
        history[2927] = 0;
        history[2928] = 0;
        history[2929] = 0;
        history[2930] = 0;
        history[2931] = 0;
        history[2932] = 0;
        history[2933] = 0;
        history[2934] = 0;
        history[2935] = 0;
        history[2936] = 0;
        history[2937] = 0;
        history[2938] = 0;
        history[2939] = 0;
        history[2940] = 0;
        history[2941] = INFINITY;
        history[2942] = 0;
        history[2943] = 0;
        history[2944] = 0;
        history[2945] = NAN;
        history[2946] = 0;
        history[2947] = NAN;
        history[2948] = 0;
        history[2949] = NAN;
        history[2950] = 0;
        history[2951] = NAN;
        history[2952] = 0;
        history[2953] = NAN;
        history[2954] = 0;
        history[2955] = NAN;
        history[2956] = 0;
        history[2957] = NAN;
        history[2958] = 0;
        history[2959] = NAN;
        history[2960] = 0;
        history[2961] = NAN;
        history[2962] = 0;
        history[2963] = NAN;
        history[2964] = 0;
        history[2965] = NAN;
        history[2966] = 0;
        history[2967] = NAN;
        history[2968] = 0;
        history[2969] = NAN;
        history[2970] = 0;
        history[2971] = NAN;
        history[2972] = 0;
        history[2973] = NAN;
        history[2974] = 0;
        history[2975] = NAN;
        history[2976] = 0;
        history[2977] = NAN;
        history[2978] = 0;
        history[2979] = NAN;
        history[2980] = 0;
        history[2981] = NAN;
        history[2982] = 0;
        history[2983] = NAN;
        history[2984] = 0;
        history[2985] = NAN;
        history[2986] = 0;
        history[2987] = NAN;
        history[2988] = 0;
        history[2989] = -INFINITY;
        history[2990] = 0;
        history[2991] = 0;
        history[2992] = 0;
        history[2993] = -INFINITY;
        history[2994] = 0;
        history[2995] = -INFINITY;
        history[2996] = 0;
        history[2997] = -INFINITY;
        history[2998] = 0;
        history[2999] = 0;
        history[3000] = 0;
        history[3001] = 0;
        history[3002] = 0;
        history[3003] = 0;
        history[3004] = 0;
        history[3005] = 0;
        history[3006] = 0;
        history[3007] = 0;
        history[3008] = 0;
        history[3009] = 0;
        history[3010] = 0;
        history[3011] = 0;
        history[3012] = 0;
        history[3013] = -INFINITY;
        history[3014] = 0;
        history[3015] = 0;
        history[3016] = 0;
        history[3017] = -INFINITY;
        history[3018] = 0;
        history[3019] = 0;
        history[3020] = 0;
        history[3021] = 0;
        history[3022] = 0;
        history[3023] = 0;
        history[3024] = 0;
        history[3025] = 0;
        history[3026] = 0;
        history[3027] = 0;
        history[3028] = 0;
        history[3029] = 0;
        history[3030] = 0;
        history[3031] = 0;
        history[3032] = -INFINITY;
        history[3033] = 0;
        history[3034] = 0;
        history[3035] = 0;
        history[3036] = 0;
        history[3037] = 0;
        history[3038] = 0;
        history[3039] = 0;
        history[3040] = 0;
        history[3041] = 0;
        history[3042] = 0;
        history[3043] = 0;
        history[3044] = 0;
        history[3045] = 0;
        history[3046] = 0;
        history[3047] = 0;
        history[3048] = 0;
        history[3049] = INFINITY;
        history[3050] = 0;
        history[3051] = 0;
        history[3052] = 0;
        history[3053] = 0;
        history[3054] = 0;
        history[3055] = INFINITY;
        history[3056] = 0;
        history[3057] = 0;
        history[3058] = 0;
        history[3059] = 0;
        history[3060] = NAN;
        history[3061] = 0;
        history[3062] = NAN;
        history[3063] = 0;
        history[3064] = NAN;
        history[3065] = 0;
        history[3066] = NAN;
        history[3067] = 0;
        history[3068] = NAN;
        history[3069] = 0;
        history[3070] = NAN;
        history[3071] = 0;
        history[3072] = NAN;
        history[3073] = 0;
        history[3074] = NAN;
        history[3075] = 0;
        history[3076] = NAN;
        history[3077] = 0;
        history[3078] = NAN;
        history[3079] = 0;
        history[3080] = NAN;
        history[3081] = 0;
        history[3082] = NAN;
        history[3083] = 0;
        history[3084] = NAN;
        history[3085] = 0;
        history[3086] = NAN;
        history[3087] = 0;
        history[3088] = NAN;
        history[3089] = 0;
        history[3090] = NAN;
        history[3091] = 0;
        history[3092] = NAN;
        history[3093] = 0;
        history[3094] = NAN;
        history[3095] = 0;
        history[3096] = NAN;
        history[3097] = 0;
        history[3098] = NAN;
        history[3099] = 0;
        history[3100] = NAN;
        history[3101] = 0;
        history[3102] = NAN;
        history[3103] = 0;
        history[3104] = NAN;
        history[3105] = 0;
        history[3106] = -INFINITY;
        history[3107] = 0;
        history[3108] = 0;
        history[3109] = 0;
        history[3110] = 0;
        history[3111] = 0;
        history[3112] = 0;
        history[3113] = 0;
        history[3114] = -INFINITY;
        history[3115] = 0;
        history[3116] = 0;
        history[3117] = 0;
        history[3118] = INFINITY;
        history[3119] = 0;
        history[3120] = 0;
        history[3121] = 0;
        history[3122] = -INFINITY;
        history[3123] = 0;
        history[3124] = -INFINITY;
        history[3125] = 0;
        history[3126] = 0;
        history[3127] = 0;
        history[3128] = 0;
        history[3129] = 0;
        history[3130] = 0;
        history[3131] = 0;
        history[3132] = 0;
        history[3133] = 0;
        history[3134] = 0;
        history[3135] = 0;
        history[3136] = 0;
        history[3137] = 0;
        history[3138] = NAN;
        history[3139] = 0;
        history[3140] = NAN;
        history[3141] = 0;
        history[3142] = NAN;
    } else if (lg == 2){
        history[3143] = 0;
        history[3144] = 0;
        history[3145] = 0;
        history[3146] = 0;
        history[3147] = 0;
        history[3148] = NAN;
        history[3149] = 0;
        history[3150] = 0;
        history[3151] = 0;
        history[3152] = 0;
        history[3153] = 0;
        history[3154] = 0;
        history[3155] = 0;
        history[3156] = NAN;
        history[3157] = 0;
        history[3158] = -INFINITY;
        history[3159] = 0;
        history[3160] = 0;
        history[3161] = 0;
        history[3162] = NAN;
        history[3163] = 0;
        history[3164] = NAN;
        history[3165] = 0;
        history[3166] = -INFINITY;
        history[3167] = 0;
        history[3168] = NAN;
        history[3169] = 0;
        history[3170] = NAN;
        history[3171] = 0;
        history[3172] = 0;
        history[3173] = 0;
        history[3174] = 0;
        history[3175] = 0;
        history[3176] = INFINITY;
        history[3177] = 0;
        history[3178] = INFINITY;
        history[3179] = 0;
        history[3180] = NAN;
        history[3181] = 0;
        history[3182] = 0;
    }
}


void fill_history(
    long lg,
    long* level,
    double* history,
    long* x_index,
    long* x_text_numerical,
    long* x_en,
    long* x_n,
    long* x_fqids,
    long* x_et,
    double* x_rc_x,
    double* x_rc_y,
    double* x_sc_x,
    double* x_sc_y,
    long* x_b,
    long* x_r,
    long* x_room_fqid_numerical,
    long* x_text_fqid_numerical,
    double* x_page,
    double* x_hover_duration,
    long n
){

    init_history(lg, history);
    
    double screen_coor_y_abs_diff1;
    double screen_coor_x_abs_diff1;
    double et_since_prev;
    float temp;
    double temp_mean;
    
    if (lg == 0){ // 0 => level_group 

        for (int i=0; i < n; i++){ // n is number of events in particular level_group (per session).
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (isnan(et_since_prev) == false){
                history[117] += 1;
            }
            if ((isnan(et_since_prev) == false) & (et_since_prev > history[118])){
                history[118] = et_since_prev;
            }
            if (isnan(x_page[i]) == false){
                history[119] += 1;
            }
            if ((isnan(x_page[i]) == false)){
                history[120] += x_page[i];
            }
            if (isnan(x_rc_x[i]) == false){
                history[121] += 1;
            }
            if ((isnan(x_rc_x[i]) == false)){
                history[122] += x_rc_x[i];
            }
            if (isnan(x_rc_y[i]) == false){
                history[123] += 1;
            }
            if ((isnan(x_rc_y[i]) == false)){
                history[124] += x_rc_y[i];
            }
            if (isnan(screen_coor_x_abs_diff1) == false){
                history[125] += 1;
            }
            if ((isnan(screen_coor_x_abs_diff1) == false)){
                history[126] += screen_coor_x_abs_diff1;
            }
            if ((isnan(screen_coor_x_abs_diff1) == false)){
                history[127] += pow(screen_coor_x_abs_diff1, 2);
            }
            if (isnan(screen_coor_y_abs_diff1) == false){
                history[128] += 1;
            }
            if ((isnan(screen_coor_y_abs_diff1) == false)){
                history[129] += screen_coor_y_abs_diff1;
            }
            if ((isnan(screen_coor_y_abs_diff1) == false)){
                history[130] += pow(screen_coor_y_abs_diff1, 2);
            }
            if (x_en[i] == 4){
                if (isnan(et_since_prev) == false){
                    history[131] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[132] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[133] += pow(et_since_prev, 2);
                }
            }
            else if (x_en[i] == 5){
                if (isnan(et_since_prev) == false){
                    history[134] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[135])){
                    history[135] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[136] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[137] += pow(et_since_prev, 2);
                }
            }
            else if (x_en[i] == 7){
                if (isnan(et_since_prev) == false){
                    history[138] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[139] += et_since_prev;
                }
            }
            else if (x_en[i] == 8){
                if (isnan(x_index[i]) == false){
                    history[140] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[141] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[142] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[143] += pow(et_since_prev, 2);
                }
            }
            else if (x_en[i] == 9){
                if (isnan(x_index[i]) == false){
                    history[144] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[145] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[146])){
                    history[146] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[147] += et_since_prev;
                }
            }
            else if (x_en[i] == 10){
                if (isnan(et_since_prev) == false){
                    history[148] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[149])){
                    history[149] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[150] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[151] += pow(et_since_prev, 2);
                }
            }
            if (x_fqids[i] == 13){
                if (isnan(et_since_prev) == false){
                    history[152] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[153] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 20){
                if (isnan(et_since_prev) == false){
                    history[154] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[155])){
                    history[155] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 21){
                if (isnan(et_since_prev) == false){
                    history[156] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[157])){
                    history[157] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[158])){
                    history[158] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[159] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 30){
                if (isnan(et_since_prev) == false){
                    history[160] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[161])){
                    history[161] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[162])){
                    history[162] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[163] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[164] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 68){
                if (isnan(et_since_prev) == false){
                    history[165] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[166])){
                    history[166] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[167] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 69){
                if (isnan(et_since_prev) == false){
                    history[168] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[169] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[170] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 70){
                if (isnan(et_since_prev) == false){
                    history[171] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[172])){
                    history[172] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[173] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 90){
                if (isnan(x_index[i]) == false){
                    history[174] += 1;
                }
            }
            else if (x_fqids[i] == 91){
                if (isnan(et_since_prev) == false){
                    history[175] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[176])){
                    history[176] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 94){
                if (isnan(et_since_prev) == false){
                    history[177] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[178])){
                    history[178] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 99){
                if (isnan(x_index[i]) == false){
                    history[179] += 1;
                }
            }
            else if (x_fqids[i] == 101){
                if (isnan(et_since_prev) == false){
                    history[180] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[181])){
                    history[181] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 103){
                if (isnan(et_since_prev) == false){
                    history[182] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[183])){
                    history[183] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[184] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 105){
                if (isnan(et_since_prev) == false){
                    history[185] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[186])){
                    history[186] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[187] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[188] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 112){
                if (isnan(x_index[i]) == false){
                    history[189] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[190] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[191])){
                    history[191] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 118){
                if (isnan(et_since_prev) == false){
                    history[192] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[193])){
                    history[193] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[194] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 119){
                if (isnan(et_since_prev) == false){
                    history[195] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[196])){
                    history[196] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 121){
                if (isnan(et_since_prev) == false){
                    history[197] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[198])){
                    history[198] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[199] += et_since_prev;
                }
            }
            if (x_n[i] == 2){
                if (isnan(x_index[i]) == false){
                    history[200] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[201] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[202] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[203] += pow(et_since_prev, 2);
                }
            }
            else if (x_n[i] == 5){
                if (isnan(et_since_prev) == false){
                    history[204] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[205])){
                    history[205] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[206])){
                    history[206] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[207] += et_since_prev;
                }
            }
            else if (x_n[i] == 3){
                if (isnan(et_since_prev) == false){
                    history[208] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[209])){
                    history[209] = et_since_prev;
                }
            }
            else if (x_n[i] == 4){
                if (isnan(et_since_prev) == false){
                    history[210] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[211])){
                    history[211] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[212])){
                    history[212] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[213] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[214] += pow(et_since_prev, 2);
                }
            }
            else if (x_n[i] == 1){
                if (isnan(et_since_prev) == false){
                    history[215] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[216] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[217] += pow(et_since_prev, 2);
                }
            }
            if (x_room_fqid_numerical[i] == 0){
                if (isnan(et_since_prev) == false){
                    history[218] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[219] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[220] += pow(et_since_prev, 2);
                }
            }
            else if (x_room_fqid_numerical[i] == 9){
                if (isnan(et_since_prev) == false){
                    history[221] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[222])){
                    history[222] = et_since_prev;
                }
            }
            else if (x_room_fqid_numerical[i] == 13){
                if (isnan(x_index[i]) == false){
                    history[223] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[224] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[225] += et_since_prev;
                }
            }
            else if (x_room_fqid_numerical[i] == 15){
                if (isnan(et_since_prev) == false){
                    history[226] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[227])){
                    history[227] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[228] += et_since_prev;
                }
            }
            if (x_text_fqid_numerical[i] == 2){
                if (isnan(et_since_prev) == false){
                    history[229] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[230] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[231] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 23){
                if (isnan(et_since_prev) == false){
                    history[232] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[233] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 33){
                if (isnan(et_since_prev) == false){
                    history[234] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[235])){
                    history[235] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 34){
                if (isnan(et_since_prev) == false){
                    history[236] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[237])){
                    history[237] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 37){
                if (isnan(et_since_prev) == false){
                    history[238] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[239])){
                    history[239] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[240] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 38){
                if (isnan(et_since_prev) == false){
                    history[241] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[242])){
                    history[242] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[243] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[244] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 52){
                if (isnan(et_since_prev) == false){
                    history[245] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[246])){
                    history[246] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[247])){
                    history[247] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 60){
                if (isnan(et_since_prev) == false){
                    history[248] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[249])){
                    history[249] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[250] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 67){
                if (isnan(et_since_prev) == false){
                    history[251] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[252] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[253] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 71){
                if (isnan(et_since_prev) == false){
                    history[254] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[255])){
                    history[255] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[256])){
                    history[256] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[257] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 90){
                if (isnan(et_since_prev) == false){
                    history[258] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[259] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 97){
                if (isnan(et_since_prev) == false){
                    history[260] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[261])){
                    history[261] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[262] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[263] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 98){
                if (isnan(et_since_prev) == false){
                    history[264] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[265])){
                    history[265] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[266] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[267] += pow(et_since_prev, 2);
                }
            }
                                  
            if (level[i] == 0){
                if (x_text_fqid_numerical[i] == 40){
                    if (isnan(x_index[i]) == false){
                        history[268] += 1;
                    }
                    if (isnan(history[269])){
                        history[269] = x_index[i];
                    }
                    history[270] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 37){
                    if (isnan(x_index[i]) == false){
                        history[271] += 1;
                    }
                    if (isnan(history[272])){
                        history[272] = x_index[i];
                    }
                    history[273] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 38){
                    if (isnan(x_index[i]) == false){
                        history[274] += 1;
                    }
                    if (isnan(history[275])){
                        history[275] = x_index[i];
                    }
                    history[276] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[277] += 1;
                    }
                    if (isnan(history[278])){
                        history[278] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 36){
                    if (isnan(x_index[i]) == false){
                        history[279] += 1;
                    }
                    if (isnan(history[280])){
                        history[280] = x_index[i];
                    }
                    history[281] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 39){
                    if (isnan(x_index[i]) == false){
                        history[282] += 1;
                    }
                    if (isnan(history[283])){
                        history[283] = x_index[i];
                    }
                    history[284] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 35){
                    if (isnan(x_index[i]) == false){
                        history[285] += 1;
                    }
                    history[286] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[287] += 1;
                    }
                    if (isnan(history[288])){
                        history[288] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 34){
                    if (isnan(x_index[i]) == false){
                        history[289] += 1;
                    }
                    if (isnan(history[290])){
                        history[290] = x_index[i];
                    }
                    history[291] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 33){
                    if (isnan(x_index[i]) == false){
                        history[292] += 1;
                    }
                    if (isnan(history[293])){
                        history[293] = x_index[i];
                    }
                }
                if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[294] += 1;
                    }
                    if (isnan(history[295])){
                        history[295] = x_index[i];
                    }
                    history[296] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[297] += 1;
                    }
                    if (isnan(history[298])){
                        history[298] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 91){
                    if (isnan(x_index[i]) == false){
                        history[299] += 1;
                    }
                    if (isnan(history[300])){
                        history[300] = x_index[i];
                    }
                    history[301] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[302] += 1;
                    }
                    if (isnan(history[303])){
                        history[303] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 70){
                    if (isnan(x_index[i]) == false){
                        history[304] += 1;
                    }
                    if (isnan(history[305])){
                        history[305] = x_index[i];
                    }
                    history[306] = x_index[i];
                }
                else if (x_fqids[i] == 34){
                    if (isnan(x_index[i]) == false){
                        history[307] += 1;
                    }
                    if (isnan(history[308])){
                        history[308] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 42){
                    if (isnan(x_index[i]) == false){
                        history[309] += 1;
                    }
                    history[310] = x_index[i];
                }
                else if (x_fqids[i] == 39){
                    if (isnan(x_index[i]) == false){
                        history[311] += 1;
                    }
                    if (isnan(history[312])){
                        history[312] = x_index[i];
                    }
                    history[313] = x_index[i];
                }
                else if (x_fqids[i] == 68){
                    if (isnan(x_index[i]) == false){
                        history[314] += 1;
                    }
                    history[315] = x_index[i];
                }
                else if (x_fqids[i] == 94){
                    if (isnan(x_index[i]) == false){
                        history[316] += 1;
                    }
                    if (isnan(history[317])){
                        history[317] = x_index[i];
                    }
                    history[318] = x_index[i];
                }
                if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[319] += 1;
                    }
                    if (isnan(history[320])){
                        history[320] = x_index[i];
                    }
                    history[321] = x_index[i];
                }
                else if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[322] += 1;
                    }
                    if (isnan(history[323])){
                        history[323] = x_index[i];
                    }
                    history[324] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[325] += 1;
                    }
                    if (isnan(history[326])){
                        history[326] = x_index[i];
                    }
                    history[327] = x_index[i];
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[328] += 1;
                    }
                    if (isnan(history[329])){
                        history[329] = x_index[i];
                    }
                    history[330] = x_index[i];
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[331] += 1;
                    }
                    if (isnan(history[332])){
                        history[332] = x_index[i];
                    }
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[333] += 1;
                    }
                    history[334] = x_index[i];
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[335] += 1;
                    }
                    history[336] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[337] += 1;
                    }
                    if (isnan(history[338])){
                        history[338] = x_index[i];
                    }
                    history[339] = x_index[i];
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[340] += 1;
                    }
                    if (isnan(history[341])){
                        history[341] = x_index[i];
                    }
                    history[342] = x_index[i];
                }
                else if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[343] += 1;
                    }
                    if (isnan(history[344])){
                        history[344] = x_index[i];
                    }
                    history[345] = x_index[i];
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[346] += 1;
                    }
                    history[347] = x_index[i];
                }
            } else if (level[i] == 1){
                if (x_text_fqid_numerical[i] == 38){
                    if (isnan(x_index[i]) == false){
                        history[348] += 1;
                    }
                    if (isnan(history[349])){
                        history[349] = x_index[i];
                    }
                    history[350] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[351] += 1;
                    }
                    if (isnan(history[352])){
                        history[352] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[353] += 1;
                    }
                    if (isnan(history[354])){
                        history[354] = x_index[i];
                    }
                    history[355] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 59){
                    if (isnan(x_index[i]) == false){
                        history[356] += 1;
                    }
                    if (isnan(history[357])){
                        history[357] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 67){
                    if (isnan(x_et[i]) == false){
                        history[358] += 1;
                    }
                    if (isnan(history[359])){
                        history[359] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[360] += 1;
                    }
                    if (isnan(history[361])){
                        history[361] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                    if (isnan(x_et[i]) == false){
                        history[362] += 1;
                    }
                    if (isnan(history[363])){
                        history[363] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[364] += 1;
                    }
                    if (isnan(history[365])){
                        history[365] = x_index[i];
                    }
                }
                if (x_fqids[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[366] += 1;
                    }
                    if (isnan(history[367])){
                        history[367] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 40){
                    if (isnan(x_index[i]) == false){
                        history[368] += 1;
                    }
                    if (isnan(history[369])){
                        history[369] = x_index[i];
                    }
                    history[370] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[371] += 1;
                    }
                    if (isnan(history[372])){
                        history[372] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 91){
                    if (isnan(x_index[i]) == false){
                        history[373] += 1;
                    }
                    if (isnan(history[374])){
                        history[374] = x_index[i];
                    }
                    history[375] = x_index[i];
                }
                else if (x_fqids[i] == 43){
                    if (isnan(x_index[i]) == false){
                        history[376] += 1;
                    }
                    history[377] = x_index[i];
                }
                else if (x_fqids[i] == 90){
                    if (isnan(x_index[i]) == false){
                        history[378] += 1;
                    }
                    if (isnan(history[379])){
                        history[379] = x_index[i];
                    }
                    history[380] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[381] += 1;
                    }
                    if (isnan(history[382])){
                        history[382] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[383] += 1;
                    }
                    history[384] = x_index[i];
                }
                else if (x_fqids[i] == 97){
                    if (isnan(x_index[i]) == false){
                        history[385] += 1;
                    }
                    history[386] = x_index[i];
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[387] += 1;
                    }
                    history[388] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[389] += 1;
                    }
                    history[390] = x_et[i];
                }
                else if (x_fqids[i] == 30){
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_et[i]) == false){
                        history[391] += 1;
                    }
                    if (isnan(history[392])){
                        history[392] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[393] += 1;
                    }
                    if (isnan(history[394])){
                        history[394] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 125){
                }
                if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[395] += 1;
                    }
                    if (isnan(history[396])){
                        history[396] = x_index[i];
                    }
                    history[397] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[398] += 1;
                    }
                    if (isnan(history[399])){
                        history[399] = x_et[i];
                    }
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[400] += 1;
                    }
                    history[401] = x_index[i];
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[402] += 1;
                    }
                    if (isnan(history[403])){
                        history[403] = x_index[i];
                    }
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[404] += 1;
                    }
                    if (isnan(history[405])){
                        history[405] = x_index[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[406] += 1;
                    }
                    if (isnan(history[407])){
                        history[407] = x_index[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (isnan(x_et[i]) == false){
                        history[408] += 1;
                    }
                    if (isnan(history[409])){
                        history[409] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[410] += 1;
                    }
                    if (isnan(history[411])){
                        history[411] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[412] += 1;
                    }
                    if (isnan(history[413])){
                        history[413] = x_index[i];
                    }
                    history[414] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[415] += 1;
                    }
                    if (isnan(history[416])){
                        history[416] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[417] += 1;
                    }
                    if (isnan(history[418])){
                        history[418] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[419] += 1;
                    }
                    if (isnan(history[420])){
                        history[420] = x_index[i];
                    }
                    if (isnan(x_et[i]) == false){
                        history[421] += 1;
                    }
                    if (isnan(history[422])){
                        history[422] = x_et[i];
                    }
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[423] += 1;
                    }
                    if (isnan(history[424])){
                        history[424] = x_index[i];
                    }
                    history[425] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[426] += 1;
                    }
                    if (isnan(history[427])){
                        history[427] = x_et[i];
                    }
                    history[428] = x_et[i];
                }
                else if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[429] += 1;
                    }
                    history[430] = x_index[i];
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[431] += 1;
                    }
                    if (isnan(history[432])){
                        history[432] = x_index[i];
                    }
                    history[433] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[434] += 1;
                    }
                    if (isnan(history[435])){
                        history[435] = x_et[i];
                    }
                }
                else if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[436] += 1;
                    }
                    if (isnan(history[437])){
                        history[437] = x_index[i];
                    }
                    history[438] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[439] += 1;
                    }
                    if (isnan(history[440])){
                        history[440] = x_et[i];
                    }
                }
            } else if (level[i] == 2){
                if (x_fqids[i] == 12){
                    if (isnan(x_index[i]) == false){
                        history[441] += 1;
                    }
                    if (isnan(history[442])){
                        history[442] = x_index[i];
                    }
                    history[443] = x_index[i];
                }
                else if (x_fqids[i] == 119){
                    if (isnan(x_index[i]) == false){
                        history[444] += 1;
                    }
                    history[445] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[446] += 1;
                    }
                    history[447] = x_et[i];
                }
                else if (x_fqids[i] == 125){
                    if (isnan(x_index[i]) == false){
                        history[448] += 1;
                    }
                    if (isnan(history[449])){
                        history[449] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 99){
                    if (isnan(x_index[i]) == false){
                        history[450] += 1;
                    }
                    history[451] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[452] += 1;
                    }
                    history[453] = x_index[i];
                }
                else if (x_fqids[i] == 112){
                    if (isnan(x_index[i]) == false){
                        history[454] += 1;
                    }
                    if (isnan(history[455])){
                        history[455] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 29){
                    if (isnan(x_index[i]) == false){
                        history[456] += 1;
                    }
                    if (isnan(history[457])){
                        history[457] = x_index[i];
                    }
                    history[458] = x_index[i];
                }
                if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[459] += 1;
                    }
                    history[460] = x_index[i];
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[461] += 1;
                    }
                    history[462] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[463] += 1;
                    }
                    if (isnan(history[464])){
                        history[464] = x_index[i];
                    }
                    history[465] = x_index[i];
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[466] += 1;
                    }
                    if (isnan(history[467])){
                        history[467] = x_index[i];
                    }
                    history[468] = x_index[i];
                }
                else if (x_en[i] == 8){
                    if (isnan(x_et[i]) == false){
                        history[469] += 1;
                    }
                    history[470] = x_et[i];
                    if (isnan(x_index[i]) == false){
                        history[471] += 1;
                    }
                    history[472] = x_index[i];
                }
                if (x_text_fqid_numerical[i] == 61){
                    if (isnan(x_index[i]) == false){
                        history[473] += 1;
                    }
                    history[474] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 51){
                    if (isnan(x_index[i]) == false){
                        history[475] += 1;
                    }
                    if (isnan(history[476])){
                        history[476] = x_index[i];
                    }
                    history[477] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[478] += 1;
                    }
                    if (isnan(history[479])){
                        history[479] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 53){
                    if (isnan(x_index[i]) == false){
                        history[480] += 1;
                    }
                    history[481] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 52){
                    if (isnan(x_index[i]) == false){
                        history[482] += 1;
                    }
                    if (isnan(history[483])){
                        history[483] = x_index[i];
                    }
                    history[484] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 38){
                    if (isnan(x_et[i]) == false){
                        history[485] += 1;
                    }
                    if (isnan(history[486])){
                        history[486] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[487] += 1;
                    }
                    if (isnan(history[488])){
                        history[488] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 55){
                    if (isnan(x_et[i]) == false){
                        history[489] += 1;
                    }
                    if (isnan(history[490])){
                        history[490] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[491] += 1;
                    }
                    if (isnan(history[492])){
                        history[492] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 56){
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[493] += 1;
                    }
                    if (isnan(history[494])){
                        history[494] = x_index[i];
                    }
                    history[495] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[496] += 1;
                    }
                    if (isnan(history[497])){
                        history[497] = x_index[i];
                    }
                    history[498] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 7){
                    if (isnan(x_et[i]) == false){
                        history[499] += 1;
                    }
                    if (isnan(history[500])){
                        history[500] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[501] += 1;
                    }
                    if (isnan(history[502])){
                        history[502] = x_index[i];
                    }
                }
                if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[503] += 1;
                    }
                    if (isnan(history[504])){
                        history[504] = x_index[i];
                    }
                    history[505] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[506] += 1;
                    }
                    if (isnan(history[507])){
                        history[507] = x_et[i];
                    }
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[508] += 1;
                    }
                    if (isnan(history[509])){
                        history[509] = x_index[i];
                    }
                    history[510] = x_index[i];
                }
                else if (x_n[i] == 1){
                }
                else if (x_n[i] == 2){
                }
            } else if (level[i] == 3){
                if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[511] += 1;
                    }
                    if (isnan(history[512])){
                        history[512] = x_index[i];
                    }
                    history[513] = x_index[i];
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[514] += 1;
                    }
                    if (isnan(history[515])){
                        history[515] = x_index[i];
                    }
                    history[516] = x_index[i];
                }
                else if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[517] += 1;
                    }
                    if (isnan(history[518])){
                        history[518] = x_index[i];
                    }
                    history[519] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[520] += 1;
                    }
                    history[521] = x_et[i];
                }
                else if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[522] += 1;
                    }
                    if (isnan(history[523])){
                        history[523] = x_index[i];
                    }
                    history[524] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[525] += 1;
                    }
                    if (isnan(history[526])){
                        history[526] = x_et[i];
                    }
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[527] += 1;
                    }
                    if (isnan(history[528])){
                        history[528] = x_index[i];
                    }
                    history[529] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[530] += 1;
                    }
                    if (isnan(history[531])){
                        history[531] = x_et[i];
                    }
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[532] += 1;
                    }
                    if (isnan(history[533])){
                        history[533] = x_index[i];
                    }
                    history[534] = x_index[i];
                }
                else if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[535] += 1;
                    }
                    if (isnan(history[536])){
                        history[536] = x_index[i];
                    }
                    if (isnan(x_et[i]) == false){
                        history[537] += 1;
                    }
                    if (isnan(history[538])){
                        history[538] = x_et[i];
                    }
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[539] += 1;
                    }
                    if (isnan(history[540])){
                        history[540] = x_index[i];
                    }
                    history[541] = x_index[i];
                }
                else if (x_en[i] == 2){
                    if (isnan(x_et[i]) == false){
                        history[542] += 1;
                    }
                    if (isnan(history[543])){
                        history[543] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[544] += 1;
                    }
                    if (isnan(history[545])){
                        history[545] = x_index[i];
                    }
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[546] += 1;
                    }
                    history[547] = x_index[i];
                }
                if (x_fqids[i] == 99){
                    if (isnan(x_index[i]) == false){
                        history[548] += 1;
                    }
                    if (isnan(history[549])){
                        history[549] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[550] += 1;
                    }
                    if (isnan(history[551])){
                        history[551] = x_index[i];
                    }
                    history[552] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[553] += 1;
                    }
                    if (isnan(history[554])){
                        history[554] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 112){
                    if (isnan(x_index[i]) == false){
                        history[555] += 1;
                    }
                    if (isnan(history[556])){
                        history[556] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 118){
                    if (isnan(x_index[i]) == false){
                        history[557] += 1;
                    }
                    if (isnan(history[558])){
                        history[558] = x_index[i];
                    }
                    history[559] = x_index[i];
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_index[i]) == false){
                        history[560] += 1;
                    }
                    if (isnan(history[561])){
                        history[561] = x_index[i];
                    }
                    history[562] = x_index[i];
                }
                else if (x_fqids[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[563] += 1;
                    }
                    history[564] = x_index[i];
                }
                else if (x_fqids[i] == 39){
                    if (isnan(x_index[i]) == false){
                        history[565] += 1;
                    }
                    if (isnan(history[566])){
                        history[566] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 97){
                    if (isnan(x_index[i]) == false){
                        history[567] += 1;
                    }
                    if (isnan(history[568])){
                        history[568] = x_index[i];
                    }
                    history[569] = x_index[i];
                }
                else if (x_fqids[i] == 107){
                    if (isnan(x_index[i]) == false){
                        history[570] += 1;
                    }
                    if (isnan(history[571])){
                        history[571] = x_index[i];
                    }
                    history[572] = x_index[i];
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[573] += 1;
                    }
                    if (isnan(history[574])){
                        history[574] = x_index[i];
                    }
                    history[575] = x_index[i];
                }
                else if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[576] += 1;
                    }
                    history[577] = x_index[i];
                }
                else if (x_fqids[i] == 103){
                    if (isnan(x_index[i]) == false){
                        history[578] += 1;
                    }
                    if (isnan(history[579])){
                        history[579] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 72){
                    if (isnan(x_index[i]) == false){
                        history[580] += 1;
                    }
                    if (isnan(history[581])){
                        history[581] = x_index[i];
                    }
                    history[582] = x_index[i];
                }
                else if (x_fqids[i] == 71){
                    if (isnan(x_index[i]) == false){
                        history[583] += 1;
                    }
                    if (isnan(history[584])){
                        history[584] = x_index[i];
                    }
                }
                if (x_text_fqid_numerical[i] == 40){
                    if (isnan(x_index[i]) == false){
                        history[585] += 1;
                    }
                    if (isnan(history[586])){
                        history[586] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[587] += 1;
                    }
                    if (isnan(history[588])){
                        history[588] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 54){
                    if (isnan(x_index[i]) == false){
                        history[589] += 1;
                    }
                    if (isnan(history[590])){
                        history[590] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                    if (isnan(x_index[i]) == false){
                        history[591] += 1;
                    }
                    if (isnan(history[592])){
                        history[592] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 97){
                    if (isnan(x_index[i]) == false){
                        history[593] += 1;
                    }
                    if (isnan(history[594])){
                        history[594] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 98){
                    if (isnan(x_index[i]) == false){
                        history[595] += 1;
                    }
                    history[596] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 38){
                    if (isnan(x_index[i]) == false){
                        history[597] += 1;
                    }
                    history[598] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 37){
                    if (isnan(x_index[i]) == false){
                        history[599] += 1;
                    }
                    history[600] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[601] += 1;
                    }
                    history[602] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[603] += 1;
                    }
                    history[604] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 15){
                    if (isnan(x_index[i]) == false){
                        history[605] += 1;
                    }
                    if (isnan(history[606])){
                        history[606] = x_index[i];
                    }
                    if (isnan(x_et[i]) == false){
                        history[607] += 1;
                    }
                    if (isnan(history[608])){
                        history[608] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[609] += 1;
                    }
                    history[610] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[611] += 1;
                    }
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[612] += 1;
                    }
                    history[613] = x_index[i];
                }
                else if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[614] += 1;
                    }
                    if (isnan(history[615])){
                        history[615] = x_index[i];
                    }
                }
                else if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[616] += 1;
                    }
                    history[617] = x_index[i];
                }
            } else if (level[i] == 4){
                if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[618] += 1;
                    }
                    if (isnan(history[619])){
                        history[619] = x_index[i];
                    }
                    history[620] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[621] += 1;
                    }
                    if (isnan(history[622])){
                        history[622] = x_index[i];
                    }
                    history[623] = x_index[i];
                }
                else if (x_fqids[i] == 20){
                    if (isnan(x_index[i]) == false){
                        history[624] += 1;
                    }
                    if (isnan(history[625])){
                        history[625] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 113){
                    if (isnan(x_index[i]) == false){
                        history[626] += 1;
                    }
                    history[627] = x_index[i];
                }
                else if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[628] += 1;
                    }
                    if (isnan(history[629])){
                        history[629] = x_index[i];
                    }
                    history[630] = x_index[i];
                }
                else if (x_fqids[i] == 21){
                    if (isnan(x_index[i]) == false){
                        history[631] += 1;
                    }
                    if (isnan(history[632])){
                        history[632] = x_index[i];
                    }
                }
                if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[633] += 1;
                    }
                    if (isnan(history[634])){
                        history[634] = x_index[i];
                    }
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[635] += 1;
                    }
                    if (isnan(history[636])){
                        history[636] = x_index[i];
                    }
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[637] += 1;
                    }
                    history[638] = x_index[i];
                }
                else if (x_en[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[639] += 1;
                    }
                    history[640] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[641] += 1;
                    }
                    if (isnan(history[642])){
                        history[642] = x_index[i];
                    }
                    history[643] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 15){
                    if (isnan(x_index[i]) == false){
                        history[644] += 1;
                    }
                    if (isnan(history[645])){
                        history[645] = x_index[i];
                    }
                    history[646] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[647] += 1;
                    }
                    if (isnan(history[648])){
                        history[648] = x_et[i];
                    }
                }
                if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[649] += 1;
                    }
                    if (isnan(history[650])){
                        history[650] = x_index[i];
                    }
                    history[651] = x_index[i];
                }
                else if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[652] += 1;
                    }
                    if (isnan(history[653])){
                        history[653] = x_index[i];
                    }
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[654] += 1;
                    }
                    if (isnan(history[655])){
                        history[655] = x_index[i];
                    }
                    history[656] = x_index[i];
                }
                if (x_text_fqid_numerical[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[657] += 1;
                    }
                    if (isnan(history[658])){
                        history[658] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[659] += 1;
                    }
                    history[660] = x_index[i];
                }
                if (isnan(et_since_prev) == false){
                    history[661] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[662] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[663] += pow(et_since_prev, 2);
                }
            }
        }
    } else if (lg == 1){

        for (int i=0; i < n; i++){
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (isnan(screen_coor_x_abs_diff1) == false){
                history[664] += 1;
            }
            if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[665])){
                history[665] = screen_coor_x_abs_diff1;
            }
            if ((isnan(screen_coor_x_abs_diff1) == false)){
                history[666] += screen_coor_x_abs_diff1;
            }
            if ((isnan(screen_coor_x_abs_diff1) == false)){
                history[667] += pow(screen_coor_x_abs_diff1, 2);
            }
            if (isnan(x_hover_duration[i]) == false){
                history[668] += 1;
            }
            if ((isnan(x_hover_duration[i]) == false)){
                history[669] += x_hover_duration[i];
            }
            if ((isnan(x_hover_duration[i]) == false)){
                history[670] += pow(x_hover_duration[i], 2);
            }
            if (isnan(x_rc_y[i]) == false){
                history[671] += 1;
            }
            if ((isnan(x_rc_y[i]) == false)){
                history[672] += x_rc_y[i];
            }
            if (x_en[i] == 1){
                if (isnan(et_since_prev) == false){
                    history[673] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[674] += et_since_prev;
                }
            }
            else if (x_en[i] == 4){
                if (isnan(et_since_prev) == false){
                    history[675] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[676])){
                    history[676] = et_since_prev;
                }
            }
            else if (x_en[i] == 5){
                if (isnan(et_since_prev) == false){
                    history[677] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[678])){
                    history[678] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[679] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[680] += pow(et_since_prev, 2);
                }
            }
            else if (x_en[i] == 7){
                if (isnan(et_since_prev) == false){
                    history[681] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[682])){
                    history[682] = et_since_prev;
                }
            }
            else if (x_en[i] == 9){
                if (isnan(et_since_prev) == false){
                    history[683] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[684])){
                    history[684] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[685])){
                    history[685] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[686] += et_since_prev;
                }
            }
            if (x_fqids[i] == 6){
                if (isnan(et_since_prev) == false){
                    history[687] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[688])){
                    history[688] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[689] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[690] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 14){
                if (isnan(et_since_prev) == false){
                    history[691] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[692] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 15){
                if (isnan(et_since_prev) == false){
                    history[693] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[694])){
                    history[694] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[695] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[696] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 16){
                if (isnan(et_since_prev) == false){
                    history[697] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[698])){
                    history[698] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[699] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[700] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 17){
                if (isnan(et_since_prev) == false){
                    history[701] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[702])){
                    history[702] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[703] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 18){
                if (isnan(et_since_prev) == false){
                    history[704] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[705])){
                    history[705] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 30){
                if (isnan(et_since_prev) == false){
                    history[706] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[707] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 32){
                if (isnan(et_since_prev) == false){
                    history[708] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[709] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 39){
                if (isnan(et_since_prev) == false){
                    history[710] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[711] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 44){
                if (isnan(x_index[i]) == false){
                    history[712] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[713] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[714] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 45){
                if (isnan(et_since_prev) == false){
                    history[715] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[716])){
                    history[716] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[717] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 46){
                if (isnan(et_since_prev) == false){
                    history[718] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[719])){
                    history[719] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[720] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[721] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 47){
                if (isnan(et_since_prev) == false){
                    history[722] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[723])){
                    history[723] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[724])){
                    history[724] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[725] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[726] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 48){
                if (isnan(et_since_prev) == false){
                    history[727] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[728])){
                    history[728] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 49){
                if (isnan(et_since_prev) == false){
                    history[729] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[730])){
                    history[730] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[731] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[732] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 65){
                if (isnan(et_since_prev) == false){
                    history[733] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[734])){
                    history[734] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[735] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[736] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 70){
                if (isnan(et_since_prev) == false){
                    history[737] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[738])){
                    history[738] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[739] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 75){
                if (isnan(et_since_prev) == false){
                    history[740] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[741])){
                    history[741] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[742] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 76){
                if (isnan(et_since_prev) == false){
                    history[743] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[744])){
                    history[744] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[745])){
                    history[745] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[746] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 77){
                if (isnan(et_since_prev) == false){
                    history[747] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[748])){
                    history[748] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 78){
                if (isnan(et_since_prev) == false){
                    history[749] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[750])){
                    history[750] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[751])){
                    history[751] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[752] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[753] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 79){
                if (isnan(et_since_prev) == false){
                    history[754] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[755] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 95){
                if (isnan(et_since_prev) == false){
                    history[756] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[757] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 98){
                if (isnan(et_since_prev) == false){
                    history[758] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[759])){
                    history[759] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[760])){
                    history[760] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[761] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 101){
                if (isnan(et_since_prev) == false){
                    history[762] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[763])){
                    history[763] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[764] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 104){
                if (isnan(et_since_prev) == false){
                    history[765] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[766])){
                    history[766] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 105){
                if (isnan(x_index[i]) == false){
                    history[767] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[768] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[769])){
                    history[769] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 107){
                if (isnan(et_since_prev) == false){
                    history[770] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[771] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 110){
                if (isnan(et_since_prev) == false){
                    history[772] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[773])){
                    history[773] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[774] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 122){
                if (isnan(et_since_prev) == false){
                    history[775] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[776] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[777] += pow(et_since_prev, 2);
                }
            }
            else if (x_fqids[i] == 126){
                if (isnan(et_since_prev) == false){
                    history[778] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[779] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 127){
                if (isnan(et_since_prev) == false){
                    history[780] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[781])){
                    history[781] = et_since_prev;
                }
            }
            
            if (x_n[i] == 2){
                if (isnan(et_since_prev) == false){
                    history[782] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[783])){
                    history[783] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[784] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[785] += pow(et_since_prev, 2);
                }
            }
            else if (x_n[i] == 1){
                if (isnan(x_index[i]) == false){
                    history[786] += 1;
                }
            }
            if (x_room_fqid_numerical[i] == 3){
                if (isnan(et_since_prev) == false){
                    history[787] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[788])){
                    history[788] = et_since_prev;
                }
            }
            else if (x_room_fqid_numerical[i] == 8){
                if (isnan(x_index[i]) == false){
                    history[789] += 1;
                }
                if (isnan(et_since_prev) == false){
                    history[790] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[791])){
                    history[791] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[792] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[793] += pow(et_since_prev, 2);
                }
            }
            else if (x_room_fqid_numerical[i] == 16){
                if (isnan(et_since_prev) == false){
                    history[794] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[795] += et_since_prev;
                }
            }
            else if (x_room_fqid_numerical[i] == 17){
                if (isnan(et_since_prev) == false){
                    history[796] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[797] += et_since_prev;
                }
            }
            if (x_text_fqid_numerical[i] == 1){
                if (isnan(et_since_prev) == false){
                    history[798] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[799])){
                    history[799] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[800] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 10){
                if (isnan(et_since_prev) == false){
                    history[801] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[802])){
                    history[802] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 13){
                if (isnan(et_since_prev) == false){
                    history[803] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[804])){
                    history[804] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[805] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[806] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 23){
                if (isnan(et_since_prev) == false){
                    history[807] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[808] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 41){
                if (isnan(et_since_prev) == false){
                    history[809] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[810] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 44){
                if (isnan(et_since_prev) == false){
                    history[811] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[812])){
                    history[812] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[813])){
                    history[813] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[814] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[815] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 45){
                if (isnan(et_since_prev) == false){
                    history[816] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[817])){
                    history[817] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[818])){
                    history[818] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[819] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[820] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 47){
                if (isnan(et_since_prev) == false){
                    history[821] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[822])){
                    history[822] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[823])){
                    history[823] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[824] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 48){
                if (isnan(et_since_prev) == false){
                    history[825] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[826])){
                    history[826] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[827])){
                    history[827] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[828] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[829] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 50){
                if (isnan(et_since_prev) == false){
                    history[830] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[831])){
                    history[831] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[832] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 72){
                if (isnan(et_since_prev) == false){
                    history[833] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[834])){
                    history[834] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[835] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[836] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 74){
                if (isnan(et_since_prev) == false){
                    history[837] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[838])){
                    history[838] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 78){
                if (isnan(et_since_prev) == false){
                    history[839] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[840])){
                    history[840] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[841] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 85){
                if (isnan(et_since_prev) == false){
                    history[842] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[843])){
                    history[843] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 86){
                if (isnan(et_since_prev) == false){
                    history[844] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[845])){
                    history[845] = et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 107){
                if (isnan(et_since_prev) == false){
                    history[846] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[847] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[848] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 114){
                if (isnan(et_since_prev) == false){
                    history[849] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[850])){
                    history[850] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[851] += et_since_prev;
                }
            }
            if (level[i] == 5){
                if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[852] += 1;
                    }
                    if (isnan(history[853])){
                        history[853] = x_index[i];
                    }
                    history[854] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[855] += 1;
                    }
                    if (isnan(history[856])){
                        history[856] = x_et[i];
                    }
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[857] += 1;
                    }
                    if (isnan(history[858])){
                        history[858] = x_index[i];
                    }
                    history[859] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[860] += 1;
                    }
                    if (isnan(history[861])){
                        history[861] = x_et[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[862] += 1;
                    }
                    if (isnan(history[863])){
                        history[863] = x_index[i];
                    }
                    history[864] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[865] += 1;
                    }
                    history[866] = x_index[i];
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[867] += 1;
                    }
                    if (isnan(history[868])){
                        history[868] = x_index[i];
                    }
                    history[869] = x_index[i];
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[870] += 1;
                    }
                    if (isnan(history[871])){
                        history[871] = x_index[i];
                    }
                    history[872] = x_index[i];
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[873] += 1;
                    }
                    if (isnan(history[874])){
                        history[874] = x_index[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (isnan(x_et[i]) == false){
                        history[875] += 1;
                    }
                    if (isnan(history[876])){
                        history[876] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[877] += 1;
                    }
                    if (isnan(history[878])){
                        history[878] = x_index[i];
                    }
                }
                if (x_fqids[i] == 69){
                    if (isnan(x_index[i]) == false){
                        history[879] += 1;
                    }
                    history[880] = x_index[i];
                }
                else if (x_fqids[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[881] += 1;
                    }
                    if (isnan(history[882])){
                        history[882] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 107){
                    if (isnan(x_index[i]) == false){
                        history[883] += 1;
                    }
                    if (isnan(history[884])){
                        history[884] = x_index[i];
                    }
                    history[885] = x_index[i];
                }
                else if (x_fqids[i] == 98){
                    if (isnan(x_index[i]) == false){
                        history[886] += 1;
                    }
                    if (isnan(history[887])){
                        history[887] = x_index[i];
                    }
                    history[888] = x_index[i];
                }
                else if (x_fqids[i] == 119){
                    if (isnan(x_index[i]) == false){
                        history[889] += 1;
                    }
                    if (isnan(history[890])){
                        history[890] = x_index[i];
                    }
                    history[891] = x_index[i];
                }
                else if (x_fqids[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[892] += 1;
                    }
                    history[893] = x_index[i];
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_index[i]) == false){
                        history[894] += 1;
                    }
                    if (isnan(history[895])){
                        history[895] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[896] += 1;
                    }
                    if (isnan(history[897])){
                        history[897] = x_index[i];
                    }
                    history[898] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[899] += 1;
                    }
                    if (isnan(history[900])){
                        history[900] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 113){
                    if (isnan(x_index[i]) == false){
                        history[901] += 1;
                    }
                    if (isnan(history[902])){
                        history[902] = x_index[i];
                    }
                    history[903] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[904] += 1;
                    }
                    if (isnan(history[905])){
                        history[905] = x_et[i];
                    }
                    history[906] = x_et[i];
                }
                else if (x_fqids[i] == 99){
                    if (isnan(x_index[i]) == false){
                        history[907] += 1;
                    }
                    history[908] = x_index[i];
                }
                else if (x_fqids[i] == 112){
                    if (isnan(x_index[i]) == false){
                        history[909] += 1;
                    }
                    if (isnan(history[910])){
                        history[910] = x_index[i];
                    }
                    history[911] = x_index[i];
                }
                else if (x_fqids[i] == 43){
                    if (isnan(x_index[i]) == false){
                        history[912] += 1;
                    }
                    if (isnan(history[913])){
                        history[913] = x_index[i];
                    }
                    history[914] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[915] += 1;
                    }
                    if (isnan(history[916])){
                        history[916] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 127){
                    if (isnan(x_index[i]) == false){
                        history[917] += 1;
                    }
                    if (isnan(history[918])){
                        history[918] = x_index[i];
                    }
                    history[919] = x_index[i];
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[920] += 1;
                    }
                    if (isnan(history[921])){
                        history[921] = x_index[i];
                    }
                    history[922] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[923] += 1;
                    }
                    if (isnan(history[924])){
                        history[924] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 118){
                    if (isnan(x_index[i]) == false){
                        history[925] += 1;
                    }
                    if (isnan(history[926])){
                        history[926] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[927] += 1;
                    }
                    if (isnan(history[928])){
                        history[928] = x_index[i];
                    }
                    history[929] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[930] += 1;
                    }
                    if (isnan(history[931])){
                        history[931] = x_index[i];
                    }
                    history[932] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[933] += 1;
                    }
                    history[934] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[935] += 1;
                    }
                    if (isnan(history[936])){
                        history[936] = x_index[i];
                    }
                    history[937] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[938] += 1;
                    }
                    if (isnan(history[939])){
                        history[939] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[940] += 1;
                    }
                    if (isnan(history[941])){
                        history[941] = x_index[i];
                    }
                    history[942] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[943] += 1;
                    }
                    if (isnan(history[944])){
                        history[944] = x_index[i];
                    }
                    history[945] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 15){
                    if (isnan(x_index[i]) == false){
                        history[946] += 1;
                    }
                    history[947] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[948] += 1;
                    }
                    if (isnan(history[949])){
                        history[949] = x_index[i];
                    }
                }
                if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[950] += 1;
                    }
                    if (isnan(history[951])){
                        history[951] = x_index[i];
                    }
                    history[952] = x_index[i];
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[953] += 1;
                    }
                    if (isnan(history[954])){
                        history[954] = x_index[i];
                    }
                }
                else if (x_n[i] == 3){
                    if (isnan(x_et[i]) == false){
                        history[955] += 1;
                    }
                    if (isnan(history[956])){
                        history[956] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[957] += 1;
                    }
                    if (isnan(history[958])){
                        history[958] = x_index[i];
                    }
                }
                if (x_text_fqid_numerical[i] == 50){
                    if (isnan(x_index[i]) == false){
                        history[959] += 1;
                    }
                    if (isnan(history[960])){
                        history[960] = x_index[i];
                    }
                    history[961] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 90){
                    if (isnan(x_index[i]) == false){
                        history[962] += 1;
                    }
                    if (isnan(history[963])){
                        history[963] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[964] += 1;
                    }
                    if (isnan(history[965])){
                        history[965] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[966] += 1;
                    }
                    history[967] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 23){
                }
            } else if (level[i] == 6){
                if (x_text_fqid_numerical[i] == 44){
                    if (isnan(x_index[i]) == false){
                        history[968] += 1;
                    }
                    if (isnan(history[969])){
                        history[969] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 42){
                    if (isnan(x_index[i]) == false){
                        history[970] += 1;
                    }
                    history[971] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[972] += 1;
                    }
                    if (isnan(history[973])){
                        history[973] = x_index[i];
                    }
                    history[974] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[975] += 1;
                    }
                    if (isnan(history[976])){
                        history[976] = x_index[i];
                    }
                    history[977] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 45){
                    if (isnan(x_index[i]) == false){
                        history[978] += 1;
                    }
                    if (isnan(history[979])){
                        history[979] = x_index[i];
                    }
                    history[980] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 43){
                    if (isnan(x_index[i]) == false){
                        history[981] += 1;
                    }
                    if (isnan(history[982])){
                        history[982] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 48){
                    if (isnan(x_index[i]) == false){
                        history[983] += 1;
                    }
                    if (isnan(history[984])){
                        history[984] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 49){
                    if (isnan(x_index[i]) == false){
                        history[985] += 1;
                    }
                    history[986] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[987] += 1;
                    }
                    history[988] = x_et[i];
                }
                else if (x_text_fqid_numerical[i] == 41){
                    if (isnan(x_index[i]) == false){
                        history[989] += 1;
                    }
                    history[990] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 82){
                    if (isnan(x_index[i]) == false){
                        history[991] += 1;
                    }
                    history[992] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 47){
                    if (isnan(x_index[i]) == false){
                        history[993] += 1;
                    }
                    if (isnan(history[994])){
                        history[994] = x_index[i];
                    }
                    history[995] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 73){
                    if (isnan(x_et[i]) == false){
                        history[996] += 1;
                    }
                    if (isnan(history[997])){
                        history[997] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[998] += 1;
                    }
                    if (isnan(history[999])){
                        history[999] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 75){
                    if (isnan(x_et[i]) == false){
                        history[1000] += 1;
                    }
                    if (isnan(history[1001])){
                        history[1001] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1002] += 1;
                    }
                    if (isnan(history[1003])){
                        history[1003] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 76){
                    if (isnan(x_et[i]) == false){
                        history[1004] += 1;
                    }
                    if (isnan(history[1005])){
                        history[1005] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1006] += 1;
                    }
                    if (isnan(history[1007])){
                        history[1007] = x_index[i];
                    }
                }
                if (x_fqids[i] == 118){
                    if (isnan(x_index[i]) == false){
                        history[1008] += 1;
                    }
                    if (isnan(history[1009])){
                        history[1009] = x_index[i];
                    }
                    history[1010] = x_index[i];
                }
                else if (x_fqids[i] == 98){
                    if (isnan(x_index[i]) == false){
                        history[1011] += 1;
                    }
                    history[1012] = x_index[i];
                }
                else if (x_fqids[i] == 66){
                    if (isnan(x_index[i]) == false){
                        history[1013] += 1;
                    }
                    history[1014] = x_index[i];
                }
                else if (x_fqids[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[1015] += 1;
                    }
                    if (isnan(history[1016])){
                        history[1016] = x_index[i];
                    }
                    history[1017] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1018] += 1;
                    }
                    if (isnan(history[1019])){
                        history[1019] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[1020] += 1;
                    }
                    history[1021] = x_index[i];
                }
                else if (x_fqids[i] == 70){
                    if (isnan(x_index[i]) == false){
                        history[1022] += 1;
                    }
                    if (isnan(history[1023])){
                        history[1023] = x_index[i];
                    }
                    history[1024] = x_index[i];
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_index[i]) == false){
                        history[1025] += 1;
                    }
                    history[1026] = x_index[i];
                }
                else if (x_fqids[i] == 111){
                    if (isnan(x_index[i]) == false){
                        history[1027] += 1;
                    }
                    if (isnan(history[1028])){
                        history[1028] = x_index[i];
                    }
                    history[1029] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_et[i]) == false){
                        history[1030] += 1;
                    }
                    if (isnan(history[1031])){
                        history[1031] = x_et[i];
                    }
                    history[1032] = x_et[i];
                    if (isnan(x_index[i]) == false){
                        history[1033] += 1;
                    }
                    if (isnan(history[1034])){
                        history[1034] = x_index[i];
                    }
                    history[1035] = x_index[i];
                }
                else if (x_fqids[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1036] += 1;
                    }
                    if (isnan(history[1037])){
                        history[1037] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1038] += 1;
                    }
                    if (isnan(history[1039])){
                        history[1039] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 107){
                    if (isnan(x_et[i]) == false){
                        history[1040] += 1;
                    }
                    if (isnan(history[1041])){
                        history[1041] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1042] += 1;
                    }
                    if (isnan(history[1043])){
                        history[1043] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 119){
                    if (isnan(x_et[i]) == false){
                        history[1044] += 1;
                    }
                    if (isnan(history[1045])){
                        history[1045] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1046] += 1;
                    }
                    if (isnan(history[1047])){
                        history[1047] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 8){
                }
                else if (x_fqids[i] == 110){
                }
                else if (x_fqids[i] == 102){
                }
                if (x_room_fqid_numerical[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1048] += 1;
                    }
                    if (isnan(history[1049])){
                        history[1049] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 12){
                    if (isnan(x_index[i]) == false){
                        history[1050] += 1;
                    }
                    if (isnan(history[1051])){
                        history[1051] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[1052] += 1;
                    }
                    if (isnan(history[1053])){
                        history[1053] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1054] += 1;
                    }
                    if (isnan(history[1055])){
                        history[1055] = x_index[i];
                    }
                    history[1056] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1057] += 1;
                    }
                    if (isnan(history[1058])){
                        history[1058] = x_et[i];
                    }
                }
                if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1059] += 1;
                    }
                    if (isnan(history[1060])){
                        history[1060] = x_index[i];
                    }
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[1061] += 1;
                    }
                    history[1062] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1063] += 1;
                    }
                    history[1064] = x_et[i];
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[1065] += 1;
                    }
                    history[1066] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1067] += 1;
                    }
                    history[1068] = x_index[i];
                }
                else if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1069] += 1;
                    }
                    if (isnan(history[1070])){
                        history[1070] = x_index[i];
                    }
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1071] += 1;
                    }
                    if (isnan(history[1072])){
                        history[1072] = x_index[i];
                    }
                    history[1073] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1074] += 1;
                    }
                    if (isnan(history[1075])){
                        history[1075] = x_et[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1076] += 1;
                    }
                    if (isnan(history[1077])){
                        history[1077] = x_index[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1078] += 1;
                    }
                    history[1079] = x_index[i];
                }
                else if (x_en[i] == 10){
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1080] += 1;
                    }
                    if (isnan(history[1081])){
                        history[1081] = x_index[i];
                    }
                    history[1082] = x_index[i];
                }
                else if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1083] += 1;
                    }
                    if (isnan(history[1084])){
                        history[1084] = x_index[i];
                    }
                }
                else if (x_n[i] == 5){
                }
                else if (x_n[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1085] += 1;
                    }
                    if (isnan(history[1086])){
                        history[1086] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1087] += 1;
                    }
                    if (isnan(history[1088])){
                        history[1088] = x_index[i];
                    }
                }
                else if (x_n[i] == 0){
                }
                if (isnan(et_since_prev) == false){
                    history[1089] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1090])){
                    history[1090] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1091] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1092] += pow(et_since_prev, 2);
                }
            } else if (level[i] == 7){
                if (x_fqids[i] == 18){
                    if (isnan(x_index[i]) == false){
                        history[1093] += 1;
                    }
                    if (isnan(history[1094])){
                        history[1094] = x_index[i];
                    }
                    history[1095] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1096] += 1;
                    }
                    if (isnan(history[1097])){
                        history[1097] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 14){
                    if (isnan(x_index[i]) == false){
                        history[1098] += 1;
                    }
                    if (isnan(history[1099])){
                        history[1099] = x_index[i];
                    }
                    history[1100] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1101] += 1;
                    }
                    if (isnan(history[1102])){
                        history[1102] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 128){
                    if (isnan(x_index[i]) == false){
                        history[1103] += 1;
                    }
                    if (isnan(history[1104])){
                        history[1104] = x_index[i];
                    }
                    history[1105] = x_index[i];
                }
                else if (x_fqids[i] == 17){
                    if (isnan(x_index[i]) == false){
                        history[1106] += 1;
                    }
                    if (isnan(history[1107])){
                        history[1107] = x_index[i];
                    }
                    history[1108] = x_index[i];
                }
                else if (x_fqids[i] == 15){
                    if (isnan(x_index[i]) == false){
                        history[1109] += 1;
                    }
                    if (isnan(history[1110])){
                        history[1110] = x_index[i];
                    }
                    history[1111] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1112] += 1;
                    }
                    if (isnan(history[1113])){
                        history[1113] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 107){
                    if (isnan(x_index[i]) == false){
                        history[1114] += 1;
                    }
                    if (isnan(history[1115])){
                        history[1115] = x_index[i];
                    }
                    history[1116] = x_index[i];
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[1117] += 1;
                    }
                    history[1118] = x_index[i];
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_index[i]) == false){
                        history[1119] += 1;
                    }
                    if (isnan(history[1120])){
                        history[1120] = x_index[i];
                    }
                    history[1121] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1122] += 1;
                    }
                    history[1123] = x_et[i];
                }
                else if (x_fqids[i] == 99){
                    if (isnan(x_index[i]) == false){
                        history[1124] += 1;
                    }
                    history[1125] = x_index[i];
                }
                else if (x_fqids[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1126] += 1;
                    }
                    history[1127] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1128] += 1;
                    }
                    if (isnan(history[1129])){
                        history[1129] = x_index[i];
                    }
                    history[1130] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1131] += 1;
                    }
                    if (isnan(history[1132])){
                        history[1132] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 43){
                    if (isnan(x_index[i]) == false){
                        history[1133] += 1;
                    }
                    history[1134] = x_index[i];
                }
                else if (x_fqids[i] == 120){
                    if (isnan(x_index[i]) == false){
                        history[1135] += 1;
                    }
                    history[1136] = x_index[i];
                }
                else if (x_fqids[i] == 16){
                    if (isnan(x_index[i]) == false){
                        history[1137] += 1;
                    }
                    if (isnan(history[1138])){
                        history[1138] = x_index[i];
                    }
                    history[1139] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1140] += 1;
                    }
                    history[1141] = x_et[i];
                }
                else if (x_fqids[i] == 98){
                    if (isnan(x_index[i]) == false){
                        history[1142] += 1;
                    }
                    history[1143] = x_index[i];
                }
                else if (x_fqids[i] == 39){
                    if (isnan(x_index[i]) == false){
                        history[1144] += 1;
                    }
                    if (isnan(history[1145])){
                        history[1145] = x_index[i];
                    }
                    if (isnan(x_et[i]) == false){
                        history[1146] += 1;
                    }
                    if (isnan(history[1147])){
                        history[1147] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 114){
                    if (isnan(x_et[i]) == false){
                        history[1148] += 1;
                    }
                    if (isnan(history[1149])){
                        history[1149] = x_et[i];
                    }
                    history[1150] = x_et[i];
                    if (isnan(x_index[i]) == false){
                        history[1151] += 1;
                    }
                    if (isnan(history[1152])){
                        history[1152] = x_index[i];
                    }
                    history[1153] = x_index[i];
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1154] += 1;
                    }
                    if (isnan(history[1155])){
                        history[1155] = x_index[i];
                    }
                }
                else if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1156] += 1;
                    }
                    if (isnan(history[1157])){
                        history[1157] = x_index[i];
                    }
                    history[1158] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1159] += 1;
                    }
                    history[1160] = x_et[i];
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1161] += 1;
                    }
                    if (isnan(history[1162])){
                        history[1162] = x_index[i];
                    }
                    history[1163] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1164] += 1;
                    }
                    if (isnan(history[1165])){
                        history[1165] = x_et[i];
                    }
                }
                else if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1166] += 1;
                    }
                    if (isnan(history[1167])){
                        history[1167] = x_index[i];
                    }
                    history[1168] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 12){
                    if (isnan(x_index[i]) == false){
                        history[1169] += 1;
                    }
                    if (isnan(history[1170])){
                        history[1170] = x_index[i];
                    }
                    history[1171] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[1172] += 1;
                    }
                    if (isnan(history[1173])){
                        history[1173] = x_index[i];
                    }
                    history[1174] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1175] += 1;
                    }
                    if (isnan(history[1176])){
                        history[1176] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 14){
                    if (isnan(x_index[i]) == false){
                        history[1177] += 1;
                    }
                    if (isnan(history[1178])){
                        history[1178] = x_index[i];
                    }
                    history[1179] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1180] += 1;
                    }
                    if (isnan(history[1181])){
                        history[1181] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1182] += 1;
                    }
                    if (isnan(history[1183])){
                        history[1183] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[1184] += 1;
                    }
                    if (isnan(history[1185])){
                        history[1185] = x_index[i];
                    }
                    history[1186] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[1187] += 1;
                    }
                    history[1188] = x_index[i];
                }
                if (x_text_fqid_numerical[i] == 74){
                    if (isnan(x_index[i]) == false){
                        history[1189] += 1;
                    }
                    if (isnan(history[1190])){
                        history[1190] = x_index[i];
                    }
                    history[1191] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1192] += 1;
                    }
                    if (isnan(history[1193])){
                        history[1193] = x_et[i];
                    }
                    history[1194] = x_et[i];
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1195] += 1;
                    }
                    if (isnan(history[1196])){
                        history[1196] = x_index[i];
                    }
                    history[1197] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 93){
                    if (isnan(x_index[i]) == false){
                        history[1198] += 1;
                    }
                    if (isnan(history[1199])){
                        history[1199] = x_index[i];
                    }
                    history[1200] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[1201] += 1;
                    }
                    if (isnan(history[1202])){
                        history[1202] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 46){
                    if (isnan(x_et[i]) == false){
                        history[1203] += 1;
                    }
                    if (isnan(history[1204])){
                        history[1204] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1205] += 1;
                    }
                    if (isnan(history[1206])){
                        history[1206] = x_index[i];
                    }
                }
                if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1207] += 1;
                    }
                    if (isnan(history[1208])){
                        history[1208] = x_index[i];
                    }
                    history[1209] = x_index[i];
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[1210] += 1;
                    }
                    if (isnan(history[1211])){
                        history[1211] = x_index[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1212] += 1;
                    }
                    if (isnan(history[1213])){
                        history[1213] = x_index[i];
                    }
                    history[1214] = x_index[i];
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1215] += 1;
                    }
                    if (isnan(history[1216])){
                        history[1216] = x_index[i];
                    }
                    history[1217] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1218] += 1;
                    }
                    if (isnan(history[1219])){
                        history[1219] = x_et[i];
                    }
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1220] += 1;
                    }
                    if (isnan(history[1221])){
                        history[1221] = x_index[i];
                    }
                    history[1222] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1223] += 1;
                    }
                    if (isnan(history[1224])){
                        history[1224] = x_index[i];
                    }
                    history[1225] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1226] += 1;
                    }
                    if (isnan(history[1227])){
                        history[1227] = x_et[i];
                    }
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[1228] += 1;
                    }
                    if (isnan(history[1229])){
                        history[1229] = x_index[i];
                    }
                    history[1230] = x_index[i];
                }
                else if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1231] += 1;
                    }
                    if (isnan(history[1232])){
                        history[1232] = x_index[i];
                    }
                    history[1233] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1234] += 1;
                    }
                    if (isnan(history[1235])){
                        history[1235] = x_et[i];
                    }
                    history[1236] = x_et[i];
                }
                else if (x_en[i] == 5){
                    if (isnan(x_et[i]) == false){
                        history[1237] += 1;
                    }
                    if (isnan(history[1238])){
                        history[1238] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1239] += 1;
                    }
                    if (isnan(history[1240])){
                        history[1240] = x_index[i];
                    }
                }
            } else if (level[i] == 8){
                if (x_fqids[i] == 104){
                    if (isnan(x_index[i]) == false){
                        history[1241] += 1;
                    }
                    if (isnan(history[1242])){
                        history[1242] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 65){
                    if (isnan(x_index[i]) == false){
                        history[1243] += 1;
                    }
                    if (isnan(history[1244])){
                        history[1244] = x_index[i];
                    }
                    history[1245] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1246] += 1;
                    }
                    if (isnan(history[1247])){
                        history[1247] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1248] += 1;
                    }
                    if (isnan(history[1249])){
                        history[1249] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 64){
                    if (isnan(x_index[i]) == false){
                        history[1250] += 1;
                    }
                    if (isnan(history[1251])){
                        history[1251] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 116){
                    if (isnan(x_index[i]) == false){
                        history[1252] += 1;
                    }
                    if (isnan(history[1253])){
                        history[1253] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 128){
                    if (isnan(x_et[i]) == false){
                        history[1254] += 1;
                    }
                    if (isnan(history[1255])){
                        history[1255] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1256] += 1;
                    }
                    if (isnan(history[1257])){
                        history[1257] = x_index[i];
                    }
                }
                if (x_text_fqid_numerical[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[1258] += 1;
                    }
                    if (isnan(history[1259])){
                        history[1259] = x_index[i];
                    }
                    history[1260] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1261] += 1;
                    }
                    if (isnan(history[1262])){
                        history[1262] = x_index[i];
                    }
                    history[1263] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 14){
                    if (isnan(x_index[i]) == false){
                        history[1264] += 1;
                    }
                    if (isnan(history[1265])){
                        history[1265] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1266] += 1;
                    }
                    if (isnan(history[1267])){
                        history[1267] = x_index[i];
                    }
                    history[1268] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 94){
                    if (isnan(x_et[i]) == false){
                        history[1269] += 1;
                    }
                    if (isnan(history[1270])){
                        history[1270] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1271] += 1;
                    }
                    if (isnan(history[1272])){
                        history[1272] = x_index[i];
                    }
                }
                if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1273] += 1;
                    }
                    history[1274] = x_index[i];
                }
                else if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1275] += 1;
                    }
                    if (isnan(history[1276])){
                        history[1276] = x_index[i];
                    }
                    history[1277] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1278] += 1;
                    }
                    if (isnan(history[1279])){
                        history[1279] = x_et[i];
                    }
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1280] += 1;
                    }
                    if (isnan(history[1281])){
                        history[1281] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1282] += 1;
                    }
                    if (isnan(history[1283])){
                        history[1283] = x_index[i];
                    }
                    history[1284] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1285] += 1;
                    }
                    if (isnan(history[1286])){
                        history[1286] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 14){
                    if (isnan(x_index[i]) == false){
                        history[1287] += 1;
                    }
                    history[1288] = x_index[i];
                }
                if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1289] += 1;
                    }
                    if (isnan(history[1290])){
                        history[1290] = x_index[i];
                    }
                    history[1291] = x_index[i];
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1292] += 1;
                    }
                    history[1293] = x_index[i];
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1294] += 1;
                    }
                    history[1295] = x_index[i];
                }
                else if (x_en[i] == 6){
                }
                else if (x_en[i] == 3){
                    if (isnan(x_et[i]) == false){
                        history[1296] += 1;
                    }
                    history[1297] = x_et[i];
                    if (isnan(x_index[i]) == false){
                        history[1298] += 1;
                    }
                    history[1299] = x_index[i];
                }
                if (isnan(et_since_prev) == false){
                    history[1300] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1301])){
                    history[1301] = et_since_prev;
                }
            } else if (level[i] == 9){
                if (x_fqids[i] == 116){
                    if (isnan(x_index[i]) == false){
                        history[1302] += 1;
                    }
                    if (isnan(history[1303])){
                        history[1303] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 122){
                    if (isnan(x_index[i]) == false){
                        history[1304] += 1;
                    }
                    if (isnan(history[1305])){
                        history[1305] = x_index[i];
                    }
                    history[1306] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1307] += 1;
                    }
                    if (isnan(history[1308])){
                        history[1308] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 78){
                    if (isnan(x_index[i]) == false){
                        history[1309] += 1;
                    }
                    history[1310] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1311] += 1;
                    }
                    if (isnan(history[1312])){
                        history[1312] = x_index[i];
                    }
                    history[1313] = x_index[i];
                }
                else if (x_fqids[i] == 64){
                    if (isnan(x_index[i]) == false){
                        history[1314] += 1;
                    }
                    if (isnan(history[1315])){
                        history[1315] = x_index[i];
                    }
                    history[1316] = x_index[i];
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[1317] += 1;
                    }
                    history[1318] = x_index[i];
                }
                else if (x_fqids[i] == 80){
                    if (isnan(x_index[i]) == false){
                        history[1319] += 1;
                    }
                    history[1320] = x_index[i];
                }
                else if (x_fqids[i] == 77){
                    if (isnan(x_index[i]) == false){
                        history[1321] += 1;
                    }
                    history[1322] = x_index[i];
                }
                else if (x_fqids[i] == 106){
                    if (isnan(x_index[i]) == false){
                        history[1323] += 1;
                    }
                    if (isnan(history[1324])){
                        history[1324] = x_index[i];
                    }
                    history[1325] = x_index[i];
                }
                else if (x_fqids[i] == 73){
                    if (isnan(x_index[i]) == false){
                        history[1326] += 1;
                    }
                    history[1327] = x_index[i];
                }
                else if (x_fqids[i] == 74){
                    if (isnan(x_index[i]) == false){
                        history[1328] += 1;
                    }
                    if (isnan(history[1329])){
                        history[1329] = x_index[i];
                    }
                    history[1330] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1331] += 1;
                    }
                    if (isnan(history[1332])){
                        history[1332] = x_et[i];
                    }
                    history[1333] = x_et[i];
                }
                else if (x_fqids[i] == 76){
                    if (isnan(x_index[i]) == false){
                        history[1334] += 1;
                    }
                    history[1335] = x_index[i];
                }
                else if (x_fqids[i] == 79){
                }
                else if (x_fqids[i] == 75){
                }
                if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1336] += 1;
                    }
                    if (isnan(history[1337])){
                        history[1337] = x_index[i];
                    }
                    history[1338] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1339] += 1;
                    }
                    if (isnan(history[1340])){
                        history[1340] = x_index[i];
                    }
                    history[1341] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1342] += 1;
                    }
                    if (isnan(history[1343])){
                        history[1343] = x_et[i];
                    }
                }
                else if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1344] += 1;
                    }
                    if (isnan(history[1345])){
                        history[1345] = x_index[i];
                    }
                    history[1346] = x_index[i];
                }
                else if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1347] += 1;
                    }
                    if (isnan(history[1348])){
                        history[1348] = x_index[i];
                    }
                    history[1349] = x_index[i];
                }
                else if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1350] += 1;
                    }
                    if (isnan(history[1351])){
                        history[1351] = x_index[i];
                    }
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1352] += 1;
                    }
                    if (isnan(history[1353])){
                        history[1353] = x_index[i];
                    }
                    history[1354] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1355] += 1;
                    }
                    if (isnan(history[1356])){
                        history[1356] = x_et[i];
                    }
                    history[1357] = x_et[i];
                }
                else if (x_en[i] == 10){
                }
                if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1358] += 1;
                    }
                    if (isnan(history[1359])){
                        history[1359] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[1360] += 1;
                    }
                    if (isnan(history[1361])){
                        history[1361] = x_index[i];
                    }
                    history[1362] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 114){
                    if (isnan(x_index[i]) == false){
                        history[1363] += 1;
                    }
                    if (isnan(history[1364])){
                        history[1364] = x_index[i];
                    }
                    history[1365] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 106){
                    if (isnan(x_index[i]) == false){
                        history[1366] += 1;
                    }
                    history[1367] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 16){
                    if (isnan(x_index[i]) == false){
                        history[1368] += 1;
                    }
                    if (isnan(history[1369])){
                        history[1369] = x_index[i];
                    }
                    history[1370] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1371] += 1;
                    }
                    if (isnan(history[1372])){
                        history[1372] = x_et[i];
                    }
                    history[1373] = x_et[i];
                }
                else if (x_room_fqid_numerical[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1374] += 1;
                    }
                    if (isnan(history[1375])){
                        history[1375] = x_index[i];
                    }
                    history[1376] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1377] += 1;
                    }
                    history[1378] = x_et[i];
                }
                else if (x_room_fqid_numerical[i] == 17){
                    if (isnan(x_et[i]) == false){
                        history[1379] += 1;
                    }
                    if (isnan(history[1380])){
                        history[1380] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1381] += 1;
                    }
                    if (isnan(history[1382])){
                        history[1382] = x_index[i];
                    }
                }
                if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1383] += 1;
                    }
                    if (isnan(history[1384])){
                        history[1384] = x_index[i];
                    }
                    if (isnan(x_et[i]) == false){
                        history[1385] += 1;
                    }
                    if (isnan(history[1386])){
                        history[1386] = x_et[i];
                    }
                }
                else if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1387] += 1;
                    }
                    if (isnan(history[1388])){
                        history[1388] = x_index[i];
                    }
                    history[1389] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1390] += 1;
                    }
                    if (isnan(history[1391])){
                        history[1391] = x_et[i];
                    }
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1392] += 1;
                    }
                    history[1393] = x_index[i];
                }
            } else if (level[i] == 10){
                if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1394] += 1;
                    }
                    if (isnan(history[1395])){
                        history[1395] = x_index[i];
                    }
                    history[1396] = x_index[i];
                }
                else if (x_fqids[i] == 76){
                    if (isnan(x_index[i]) == false){
                        history[1397] += 1;
                    }
                    if (isnan(history[1398])){
                        history[1398] = x_index[i];
                    }
                    history[1399] = x_index[i];
                }
                else if (x_fqids[i] == 102){
                    if (isnan(x_index[i]) == false){
                        history[1400] += 1;
                    }
                    if (isnan(history[1401])){
                        history[1401] = x_index[i];
                    }
                    history[1402] = x_index[i];
                }
                else if (x_fqids[i] == 74){
                    if (isnan(x_index[i]) == false){
                        history[1403] += 1;
                    }
                    if (isnan(history[1404])){
                        history[1404] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1405] += 1;
                    }
                    history[1406] = x_index[i];
                }
                else if (x_fqids[i] == 126){
                    if (isnan(x_index[i]) == false){
                        history[1407] += 1;
                    }
                    if (isnan(history[1408])){
                        history[1408] = x_index[i];
                    }
                    history[1409] = x_index[i];
                }
                else if (x_fqids[i] == 128){
                    if (isnan(x_index[i]) == false){
                        history[1410] += 1;
                    }
                    if (isnan(history[1411])){
                        history[1411] = x_index[i];
                    }
                    history[1412] = x_index[i];
                }
                else if (x_fqids[i] == 75){
                    if (isnan(x_et[i]) == false){
                        history[1413] += 1;
                    }
                    if (isnan(history[1414])){
                        history[1414] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1415] += 1;
                    }
                    if (isnan(history[1416])){
                        history[1416] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 73){
                }
                if (x_text_fqid_numerical[i] == 100){
                    if (isnan(x_index[i]) == false){
                        history[1417] += 1;
                    }
                    history[1418] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 102){
                    if (isnan(x_index[i]) == false){
                        history[1419] += 1;
                    }
                    if (isnan(history[1420])){
                        history[1420] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 103){
                    if (isnan(x_index[i]) == false){
                        history[1421] += 1;
                    }
                    if (isnan(history[1422])){
                        history[1422] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 111){
                    if (isnan(x_index[i]) == false){
                        history[1423] += 1;
                    }
                    if (isnan(history[1424])){
                        history[1424] = x_index[i];
                    }
                    history[1425] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1426] += 1;
                    }
                    if (isnan(history[1427])){
                        history[1427] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1428] += 1;
                    }
                    if (isnan(history[1429])){
                        history[1429] = x_index[i];
                    }
                    history[1430] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1431] += 1;
                    }
                    if (isnan(history[1432])){
                        history[1432] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 99){
                    if (isnan(x_et[i]) == false){
                        history[1433] += 1;
                    }
                    if (isnan(history[1434])){
                        history[1434] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1435] += 1;
                    }
                    if (isnan(history[1436])){
                        history[1436] = x_index[i];
                    }
                }
                if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[1437] += 1;
                    }
                    if (isnan(history[1438])){
                        history[1438] = x_index[i];
                    }
                    history[1439] = x_index[i];
                }
                else if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1440] += 1;
                    }
                    if (isnan(history[1441])){
                        history[1441] = x_index[i];
                    }
                    history[1442] = x_index[i];
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1443] += 1;
                    }
                    if (isnan(history[1444])){
                        history[1444] = x_index[i];
                    }
                    history[1445] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1446] += 1;
                    }
                    if (isnan(history[1447])){
                        history[1447] = x_et[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1448] += 1;
                    }
                    history[1449] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1450] += 1;
                    }
                    if (isnan(history[1451])){
                        history[1451] = x_index[i];
                    }
                    history[1452] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1453] += 1;
                    }
                    if (isnan(history[1454])){
                        history[1454] = x_et[i];
                    }
                }
                else if (x_en[i] == 9){
                    if (isnan(x_index[i]) == false){
                        history[1455] += 1;
                    }
                    history[1456] = x_index[i];
                }
                else if (x_en[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1457] += 1;
                    }
                    if (isnan(history[1458])){
                        history[1458] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1459] += 1;
                    }
                    if (isnan(history[1460])){
                        history[1460] = x_index[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (isnan(x_et[i]) == false){
                        history[1461] += 1;
                    }
                    if (isnan(history[1462])){
                        history[1462] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1463] += 1;
                    }
                    if (isnan(history[1464])){
                        history[1464] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 17){
                    if (isnan(x_index[i]) == false){
                        history[1465] += 1;
                    }
                    if (isnan(history[1466])){
                        history[1466] = x_index[i];
                    }
                    history[1467] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1468] += 1;
                    }
                    if (isnan(history[1469])){
                        history[1469] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 16){
                    if (isnan(x_index[i]) == false){
                        history[1470] += 1;
                    }
                    if (isnan(history[1471])){
                        history[1471] = x_index[i];
                    }
                    history[1472] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1473] += 1;
                    }
                    if (isnan(history[1474])){
                        history[1474] = x_et[i];
                    }
                }
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1475] += 1;
                    }
                    history[1476] = x_index[i];
                }
                else if (x_n[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1477] += 1;
                    }
                    history[1478] = x_et[i];
                    if (isnan(x_index[i]) == false){
                        history[1479] += 1;
                    }
                    history[1480] = x_index[i];
                }
                if (isnan(et_since_prev) == false){
                    history[1481] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1482] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1483] += pow(et_since_prev, 2);
                }
            } else if (level[i] == 11){
                if (x_text_fqid_numerical[i] == 112){
                    if (isnan(x_index[i]) == false){
                        history[1484] += 1;
                    }
                    if (isnan(history[1485])){
                        history[1485] = x_index[i];
                    }
                    history[1486] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1487] += 1;
                    }
                    if (isnan(history[1488])){
                        history[1488] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 79){
                    if (isnan(x_index[i]) == false){
                        history[1489] += 1;
                    }
                    history[1490] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 86){
                    if (isnan(x_index[i]) == false){
                        history[1491] += 1;
                    }
                    history[1492] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1493] += 1;
                    }
                    if (isnan(history[1494])){
                        history[1494] = x_index[i];
                    }
                    history[1495] = x_index[i];
                }
                else if (x_text_fqid_numerical[i] == 78){
                    if (isnan(x_et[i]) == false){
                        history[1496] += 1;
                    }
                    if (isnan(history[1497])){
                        history[1497] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1498] += 1;
                    }
                    if (isnan(history[1499])){
                        history[1499] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                }
                if (x_fqids[i] == 39){
                    if (isnan(x_index[i]) == false){
                        history[1500] += 1;
                    }
                    if (isnan(history[1501])){
                        history[1501] = x_index[i];
                    }
                    history[1502] = x_index[i];
                }
                else if (x_fqids[i] == 45){
                    if (isnan(x_index[i]) == false){
                        history[1503] += 1;
                    }
                    if (isnan(history[1504])){
                        history[1504] = x_index[i];
                    }
                    history[1505] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1506] += 1;
                    }
                    if (isnan(history[1507])){
                        history[1507] = x_index[i];
                    }
                    history[1508] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1509] += 1;
                    }
                    if (isnan(history[1510])){
                        history[1510] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 48){
                    if (isnan(x_index[i]) == false){
                        history[1511] += 1;
                    }
                    if (isnan(history[1512])){
                        history[1512] = x_index[i];
                    }
                    history[1513] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1514] += 1;
                    }
                    if (isnan(history[1515])){
                        history[1515] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_index[i]) == false){
                        history[1516] += 1;
                    }
                    if (isnan(history[1517])){
                        history[1517] = x_index[i];
                    }
                    history[1518] = x_index[i];
                }
                else if (x_fqids[i] == 118){
                    if (isnan(x_index[i]) == false){
                        history[1519] += 1;
                    }
                    history[1520] = x_index[i];
                }
                else if (x_fqids[i] == 46){
                    if (isnan(x_index[i]) == false){
                        history[1521] += 1;
                    }
                    if (isnan(history[1522])){
                        history[1522] = x_index[i];
                    }
                    history[1523] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1524] += 1;
                    }
                    history[1525] = x_et[i];
                }
                else if (x_fqids[i] == 128){
                    if (isnan(x_index[i]) == false){
                        history[1526] += 1;
                    }
                    history[1527] = x_index[i];
                }
                else if (x_fqids[i] == 114){
                    if (isnan(x_index[i]) == false){
                        history[1528] += 1;
                    }
                    if (isnan(history[1529])){
                        history[1529] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 116){
                    if (isnan(x_index[i]) == false){
                        history[1530] += 1;
                    }
                    if (isnan(history[1531])){
                        history[1531] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 47){
                    if (isnan(x_index[i]) == false){
                        history[1532] += 1;
                    }
                    if (isnan(history[1533])){
                        history[1533] = x_index[i];
                    }
                    history[1534] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1535] += 1;
                    }
                    if (isnan(history[1536])){
                        history[1536] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1537] += 1;
                    }
                    if (isnan(history[1538])){
                        history[1538] = x_index[i];
                    }
                    history[1539] = x_index[i];
                }
                else if (x_fqids[i] == 106){
                    if (isnan(x_index[i]) == false){
                        history[1540] += 1;
                    }
                    if (isnan(history[1541])){
                        history[1541] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[1542] += 1;
                    }
                    history[1543] = x_index[i];
                }
                else if (x_fqids[i] == 49){
                    if (isnan(x_index[i]) == false){
                        history[1544] += 1;
                    }
                    if (isnan(history[1545])){
                        history[1545] = x_index[i];
                    }
                    history[1546] = x_index[i];
                }
                else if (x_fqids[i] == 43){
                    if (isnan(x_index[i]) == false){
                        history[1547] += 1;
                    }
                    if (isnan(history[1548])){
                        history[1548] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 101){
                    if (isnan(x_index[i]) == false){
                        history[1549] += 1;
                    }
                    history[1550] = x_index[i];
                }
                else if (x_fqids[i] == 18){
                    if (isnan(x_et[i]) == false){
                        history[1551] += 1;
                    }
                    if (isnan(history[1552])){
                        history[1552] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1553] += 1;
                    }
                    if (isnan(history[1554])){
                        history[1554] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 122){
                }
                else if (x_fqids[i] == 44){
                }
                else if (x_fqids[i] == 120){
                }
                if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1555] += 1;
                    }
                    if (isnan(history[1556])){
                        history[1556] = x_index[i];
                    }
                    history[1557] = x_index[i];
                }
                else if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1558] += 1;
                    }
                    if (isnan(history[1559])){
                        history[1559] = x_index[i];
                    }
                    history[1560] = x_index[i];
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1561] += 1;
                    }
                    if (isnan(history[1562])){
                        history[1562] = x_index[i];
                    }
                    history[1563] = x_index[i];
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[1564] += 1;
                    }
                    history[1565] = x_index[i];
                }
                else if (x_en[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1566] += 1;
                    }
                    if (isnan(history[1567])){
                        history[1567] = x_index[i];
                    }
                    history[1568] = x_index[i];
                }
                else if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1569] += 1;
                    }
                    if (isnan(history[1570])){
                        history[1570] = x_index[i];
                    }
                }
                else if (x_en[i] == 3){
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1571] += 1;
                    }
                    if (isnan(history[1572])){
                        history[1572] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[1573] += 1;
                    }
                    if (isnan(history[1574])){
                        history[1574] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 17){
                    if (isnan(x_index[i]) == false){
                        history[1575] += 1;
                    }
                    history[1576] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1577] += 1;
                    }
                    history[1578] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 15){
                    if (isnan(x_index[i]) == false){
                        history[1579] += 1;
                    }
                    if (isnan(history[1580])){
                        history[1580] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 16){
                    if (isnan(x_index[i]) == false){
                        history[1581] += 1;
                    }
                    if (isnan(history[1582])){
                        history[1582] = x_index[i];
                    }
                    history[1583] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1584] += 1;
                    }
                    if (isnan(history[1585])){
                        history[1585] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1586] += 1;
                    }
                    if (isnan(history[1587])){
                        history[1587] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1588] += 1;
                    }
                    if (isnan(history[1589])){
                        history[1589] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 3){
                    if (isnan(x_et[i]) == false){
                        history[1590] += 1;
                    }
                    if (isnan(history[1591])){
                        history[1591] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1592] += 1;
                    }
                    if (isnan(history[1593])){
                        history[1593] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 13){
                    if (isnan(x_et[i]) == false){
                        history[1594] += 1;
                    }
                    if (isnan(history[1595])){
                        history[1595] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1596] += 1;
                    }
                    if (isnan(history[1597])){
                        history[1597] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 12){
                    if (isnan(x_index[i]) == false){
                        history[1598] += 1;
                    }
                    history[1599] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 8){
                }
                if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1600] += 1;
                    }
                    if (isnan(history[1601])){
                        history[1601] = x_index[i];
                    }
                    history[1602] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1603] += 1;
                    }
                    if (isnan(history[1604])){
                        history[1604] = x_et[i];
                    }
                    history[1605] = x_et[i];
                }
                else if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1606] += 1;
                    }
                    if (isnan(history[1607])){
                        history[1607] = x_index[i];
                    }
                    history[1608] = x_index[i];
                }
                else if (x_n[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1609] += 1;
                    }
                    if (isnan(history[1610])){
                        history[1610] = x_index[i];
                    }
                }
                else if (x_n[i] == 5){
                    if (isnan(x_et[i]) == false){
                        history[1611] += 1;
                    }
                    if (isnan(history[1612])){
                        history[1612] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1613] += 1;
                    }
                    if (isnan(history[1614])){
                        history[1614] = x_index[i];
                    }
                }
                else if (x_n[i] == 2){
                }
                if (isnan(et_since_prev) == false){
                    history[1615] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1616])){
                    history[1616] = et_since_prev;
                }
            } else if (level[i] == 12){
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1617] += 1;
                    }
                    if (isnan(history[1618])){
                        history[1618] = x_index[i];
                    }
                }
                else if (x_n[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1619] += 1;
                    }
                    if (isnan(history[1620])){
                        history[1620] = x_index[i];
                    }
                    history[1621] = x_index[i];
                    if (isnan(x_et[i]) == false){
                        history[1622] += 1;
                    }
                    if (isnan(history[1623])){
                        history[1623] = x_et[i];
                    }
                }
                else if (x_n[i] == 1){
                    if (isnan(x_et[i]) == false){
                        history[1624] += 1;
                    }
                    if (isnan(history[1625])){
                        history[1625] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1626] += 1;
                    }
                    if (isnan(history[1627])){
                        history[1627] = x_index[i];
                    }
                }
                else if (x_n[i] == 0){
                    if (isnan(x_et[i]) == false){
                        history[1628] += 1;
                    }
                    if (isnan(history[1629])){
                        history[1629] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1630] += 1;
                    }
                    if (isnan(history[1631])){
                        history[1631] = x_index[i];
                    }
                }
                if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[1632] += 1;
                    }
                    history[1633] = x_index[i];
                }
                else if (x_fqids[i] == 107){
                    if (isnan(x_index[i]) == false){
                        history[1634] += 1;
                    }
                    if (isnan(history[1635])){
                        history[1635] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 114){
                    if (isnan(x_index[i]) == false){
                        history[1636] += 1;
                    }
                    if (isnan(history[1637])){
                        history[1637] = x_index[i];
                    }
                    history[1638] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1639] += 1;
                    }
                    if (isnan(history[1640])){
                        history[1640] = x_index[i];
                    }
                    history[1641] = x_index[i];
                }
                else if (x_fqids[i] == 102){
                    if (isnan(x_index[i]) == false){
                        history[1642] += 1;
                    }
                    if (isnan(history[1643])){
                        history[1643] = x_index[i];
                    }
                    history[1644] = x_index[i];
                }
                else if (x_fqids[i] == 116){
                    if (isnan(x_index[i]) == false){
                        history[1645] += 1;
                    }
                    history[1646] = x_index[i];
                }
                else if (x_fqids[i] == 43){
                    if (isnan(x_et[i]) == false){
                        history[1647] += 1;
                    }
                    if (isnan(history[1648])){
                        history[1648] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1649] += 1;
                    }
                    if (isnan(history[1650])){
                        history[1650] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 45){
                    if (isnan(x_et[i]) == false){
                        history[1651] += 1;
                    }
                    if (isnan(history[1652])){
                        history[1652] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1653] += 1;
                    }
                    if (isnan(history[1654])){
                        history[1654] = x_index[i];
                    }
                }
                if (x_en[i] == 3){
                    if (isnan(x_index[i]) == false){
                        history[1655] += 1;
                    }
                    if (isnan(history[1656])){
                        history[1656] = x_index[i];
                    }
                    history[1657] = x_index[i];
                }
                else if (x_en[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1658] += 1;
                    }
                    if (isnan(history[1659])){
                        history[1659] = x_index[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1660] += 1;
                    }
                    if (isnan(history[1661])){
                        history[1661] = x_index[i];
                    }
                    history[1662] = x_index[i];
                }
                else if (x_en[i] == 4){
                    if (isnan(x_index[i]) == false){
                        history[1663] += 1;
                    }
                    history[1664] = x_index[i];
                }
                else if (x_en[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1665] += 1;
                    }
                    if (isnan(history[1666])){
                        history[1666] = x_index[i];
                    }
                    history[1667] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_et[i]) == false){
                        history[1668] += 1;
                    }
                    if (isnan(history[1669])){
                        history[1669] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1670] += 1;
                    }
                    if (isnan(history[1671])){
                        history[1671] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 13){
                    if (isnan(x_index[i]) == false){
                        history[1672] += 1;
                    }
                    if (isnan(history[1673])){
                        history[1673] = x_index[i];
                    }
                    history[1674] = x_index[i];
                }
                else if (x_room_fqid_numerical[i] == 8){
                    if (isnan(x_index[i]) == false){
                        history[1675] += 1;
                    }
                    if (isnan(history[1676])){
                        history[1676] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1677] += 1;
                    }
                    if (isnan(history[1678])){
                        history[1678] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (isnan(x_index[i]) == false){
                        history[1679] += 1;
                    }
                    if (isnan(history[1680])){
                        history[1680] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1681] += 1;
                    }
                    if (isnan(history[1682])){
                        history[1682] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 12){
                    if (isnan(x_index[i]) == false){
                        history[1683] += 1;
                    }
                }
                if (x_text_fqid_numerical[i] == 46){
                    if (isnan(x_index[i]) == false){
                        history[1684] += 1;
                    }
                    if (isnan(history[1685])){
                        history[1685] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 72){
                    if (isnan(x_index[i]) == false){
                        history[1686] += 1;
                    }
                    if (isnan(history[1687])){
                        history[1687] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                }
                else if (x_text_fqid_numerical[i] == 47){
                }
            }
        }
    } else if (lg == 2){

        for (int i=0; i < n; i++){
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (x_fqids[i] == 52){
                if (isnan(et_since_prev) == false){
                    history[1688] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1689] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 54){
                if (isnan(et_since_prev) == false){
                    history[1690] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1691])){
                    history[1691] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1692] += et_since_prev;
                }
            }
            else if (x_fqids[i] == 55){
                if (isnan(et_since_prev) == false){
                    history[1693] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[1694])){
                    history[1694] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 56){
                if (isnan(x_index[i]) == false){
                    history[1695] += 1;
                }
            }
            else if (x_fqids[i] == 59){
                if (isnan(et_since_prev) == false){
                    history[1696] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[1697])){
                    history[1697] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 88){
                if (isnan(et_since_prev) == false){
                    history[1698] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[1699])){
                    history[1699] = et_since_prev;
                }
            }
            else if (x_fqids[i] == 117){
                if (isnan(et_since_prev) == false){
                    history[1700] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1701])){
                    history[1701] = et_since_prev;
                }
            }
            if (x_text_fqid_numerical[i] == 15){
                if (isnan(et_since_prev) == false){
                    history[1702] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev < history[1703])){
                    history[1703] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1704])){
                    history[1704] = et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1705] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 68){
                if (isnan(et_since_prev) == false){
                    history[1706] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1707] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1708] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 108){
                if (isnan(et_since_prev) == false){
                    history[1709] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1710] += et_since_prev;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1711] += pow(et_since_prev, 2);
                }
            }
            else if (x_text_fqid_numerical[i] == 109){
                if (isnan(et_since_prev) == false){
                    history[1712] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1713] += et_since_prev;
                }
            }
            else if (x_text_fqid_numerical[i] == 118){
                if (isnan(et_since_prev) == false){
                    history[1714] += 1;
                }
                if ((isnan(et_since_prev) == false)){
                    history[1715] += et_since_prev;
                }
            }
            if (level[i] == 13){
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1716] += 1;
                    }
                    history[1717] = x_index[i];
                }
                if (x_room_fqid_numerical[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1718] += 1;
                    }
                    if (isnan(history[1719])){
                        history[1719] = x_index[i];
                    }
                }
            } else if (level[i] == 14){
                if (isnan(et_since_prev) == false){
                    history[1720] += 1;
                }
                if ((isnan(et_since_prev) == false) & (et_since_prev > history[1721])){
                    history[1721] = et_since_prev;
                }
            } else if (level[i] == 15){
                if (x_n[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1722] += 1;
                    }
                    if (isnan(history[1723])){
                        history[1723] = x_index[i];
                    }
                }
                else if (x_n[i] == 3){
                    if (isnan(x_et[i]) == false){
                        history[1724] += 1;
                    }
                    if (isnan(history[1725])){
                        history[1725] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1726] += 1;
                    }
                    if (isnan(history[1727])){
                        history[1727] = x_index[i];
                    }
                }
                if (x_fqids[i] == 107){
                    if (isnan(x_index[i]) == false){
                        history[1728] += 1;
                    }
                    history[1729] = x_index[i];
                }
                if (x_en[i] == 3){
                }
            } else if (level[i] == 18){
                if (x_fqids[i] == 35){
                    if (isnan(x_index[i]) == false){
                        history[1730] += 1;
                    }
                    history[1731] = x_index[i];
                }
                else if (x_fqids[i] == 96){
                    if (isnan(x_index[i]) == false){
                        history[1732] += 1;
                    }
                    history[1733] = x_index[i];
                }
                if (x_en[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1734] += 1;
                    }
                    if (isnan(history[1735])){
                        history[1735] = x_index[i];
                    }
                }
                else if (x_en[i] == 10){
                    if (isnan(x_index[i]) == false){
                        history[1736] += 1;
                    }
                    if (isnan(history[1737])){
                        history[1737] = x_index[i];
                    }
                }
                else if (x_en[i] == 1){
                    if (isnan(x_index[i]) == false){
                        history[1738] += 1;
                    }
                    if (isnan(history[1739])){
                        history[1739] = x_index[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 6){
                    if (isnan(x_index[i]) == false){
                        history[1740] += 1;
                    }
                    history[1741] = x_index[i];
                }
                if (x_text_fqid_numerical[i] == 117){
                    if (isnan(x_et[i]) == false){
                        history[1742] += 1;
                    }
                    if (isnan(history[1743])){
                        history[1743] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1744] += 1;
                    }
                    if (isnan(history[1745])){
                        history[1745] = x_index[i];
                    }
                }
                if (x_n[i] == 2){
                }
            } else if (level[i] == 19){
                if (x_fqids[i] == 35){
                    if (isnan(x_index[i]) == false){
                        history[1746] += 1;
                    }
                    if (isnan(history[1747])){
                        history[1747] = x_index[i];
                    }
                }
                if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1748] += 1;
                    }
                    if (isnan(history[1749])){
                        history[1749] = x_index[i];
                    }
                }
                if (x_text_fqid_numerical[i] == 118){
                    if (isnan(x_index[i]) == false){
                        history[1750] += 1;
                    }
                    history[1751] = x_index[i];
                }
                if (x_n[i] == 0){
                    if (isnan(x_et[i]) == false){
                        history[1752] += 1;
                    }
                    if (isnan(history[1753])){
                        history[1753] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1754] += 1;
                    }
                    if (isnan(history[1755])){
                        history[1755] = x_index[i];
                    }
                }
            } else if (level[i] == 20){
                if (x_text_fqid_numerical[i] == 19){
                    if (isnan(x_index[i]) == false){
                        history[1756] += 1;
                    }
                    history[1757] = x_index[i];
                }
                if (x_fqids[i] == 81){
                    if (isnan(x_index[i]) == false){
                        history[1758] += 1;
                    }
                    if (isnan(history[1759])){
                        history[1759] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 86){
                }
                else if (x_fqids[i] == 105){
                    if (isnan(x_et[i]) == false){
                        history[1760] += 1;
                    }
                    if (isnan(history[1761])){
                        history[1761] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1762] += 1;
                    }
                    if (isnan(history[1763])){
                        history[1763] = x_index[i];
                    }
                }
                if (x_en[i] == 3){
                    if (isnan(x_et[i]) == false){
                        history[1764] += 1;
                    }
                    if (isnan(history[1765])){
                        history[1765] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1766] += 1;
                    }
                    if (isnan(history[1767])){
                        history[1767] = x_index[i];
                    }
                }
                else if (x_en[i] == 6){
                }
                else if (x_en[i] == 8){
                }
            } else if (level[i] == 21){
                if (x_fqids[i] == 121){
                    if (isnan(x_index[i]) == false){
                        history[1768] += 1;
                    }
                    if (isnan(history[1769])){
                        history[1769] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 59){
                    if (isnan(x_index[i]) == false){
                        history[1770] += 1;
                    }
                    history[1771] = x_index[i];
                }
                else if (x_fqids[i] == 0){
                    if (isnan(x_index[i]) == false){
                        history[1772] += 1;
                    }
                    history[1773] = x_index[i];
                }
                if (x_text_fqid_numerical[i] == 81){
                    if (isnan(x_index[i]) == false){
                        history[1774] += 1;
                    }
                    if (isnan(history[1775])){
                        history[1775] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 109){
                    if (isnan(x_index[i]) == false){
                        history[1776] += 1;
                    }
                    if (isnan(history[1777])){
                        history[1777] = x_index[i];
                    }
                }
                if (x_en[i] == 5){
                    if (isnan(x_index[i]) == false){
                        history[1778] += 1;
                    }
                    history[1779] = x_index[i];
                }
                else if (x_en[i] == 7){
                    if (isnan(x_index[i]) == false){
                        history[1780] += 1;
                    }
                    history[1781] = x_index[i];
                }
                if (x_n[i] == 2){
                    if (isnan(x_et[i]) == false){
                        history[1782] += 1;
                    }
                    if (isnan(history[1783])){
                        history[1783] = x_et[i];
                    }
                    if (isnan(x_index[i]) == false){
                        history[1784] += 1;
                    }
                    if (isnan(history[1785])){
                        history[1785] = x_index[i];
                    }
                }
            } else if (level[i] == 22){
                if (x_n[i] == 2){
                    if (isnan(x_index[i]) == false){
                        history[1786] += 1;
                    }
                    if (isnan(history[1787])){
                        history[1787] = x_index[i];
                    }
                }
                if (x_fqids[i] == 95){
                    if (isnan(x_index[i]) == false){
                        history[1788] += 1;
                    }
                    history[1789] = x_index[i];
                }
            }
        }
    }
    if (lg == 0){

        for (int i=0; i < n; i++){
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (level[i] == 0){
                if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[280] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[1790] += 1;
                        }
                        history[1791] = x_index[i];
                    }
                }
                if (x_fqids[i] == 91){
                    if (x_index[i] > (history[300] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1792] += 1;
                        }
                        history[1793] = x_et[i];
                    }
                    if (x_index[i] > (history[275] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1794] += 1;
                        }
                        history[1795] = x_et[i];
                    }
                }
                if (x_index[i] > (history[269] + 0.5)){
                    if (x_index[i] < (history[296] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1796] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[1797])){
                            history[1797] = x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[280] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1798] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[1799] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1800] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[1801] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[301] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1802] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[1803] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[324] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1804] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] < history[1805])){
                            history[1805] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[270] + 0.5)){
                    if (x_index[i] < (history[321] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1806] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[1807])){
                            history[1807] = x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[301] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1808] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[1809])){
                            history[1809] = x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[347] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[1810] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[1811] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[338] + 0.5)){
                    if (x_index[i] < (history[273] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[1812] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[1813])){
                            history[1813] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[329] + 0.5)){
                    if (x_index[i] < (history[296] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[1814] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[1815] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[320] + 0.5)){
                    if (x_index[i] < (history[334] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[1816] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[1817] += x_index[i];
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[1818] += pow(x_index[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[323] + 0.5)){
                    if (x_index[i] < (history[342] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1819] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[1820])){
                            history[1820] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[332] + 0.5)){
                    if (x_index[i] < (history[315] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1821] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[1822])){
                            history[1822] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[344] + 0.5)){
                    if (x_index[i] < (history[339] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1823] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[1824])){
                            history[1824] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[324] + 0.5)){
                    if (x_index[i] < (history[327] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1825] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[1826])){
                            history[1826] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[281] + 0.5)){
                    if (x_index[i] < (history[342] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1827] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[1828])){
                            history[1828] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[305] + 0.5)){
                    if (x_index[i] < (history[308] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1829] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[1830])){
                            history[1830] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[338] + 0.5)){
                    if (x_index[i] < (history[306] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1831] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[1832])){
                            history[1832] = x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1833] += x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1834] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1835] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[310] + 0.5)){
                    if (x_index[i] < (history[272] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1836] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[1837])){
                            history[1837] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[345] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1838] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[1839])){
                            history[1839] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[280] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1840] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1841] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[295] + 0.5)){
                    if (x_index[i] < (history[345] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1842] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1843] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[284] + 0.5)){
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1844] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1845] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[276] + 0.5)){
                    if (x_index[i] < (history[301] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1846] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[1847])){
                            history[1847] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[320] + 0.5)){
                    if (x_index[i] < (history[275] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1848] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1849] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1850] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[317] + 0.5)){
                    if (x_index[i] < (history[275] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1851] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1852] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1853] += pow(x_rc_y[i], 2);
                        }
                    }
                    if (x_index[i] < (history[288] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1854] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1855] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[291] + 0.5)){
                    if (x_index[i] < (history[323] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1856] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1857] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1858] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[312] + 0.5)){
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1859] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1860] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[283] + 0.5)){
                    if (x_index[i] < (history[344] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1861] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1862] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[313] + 0.5)){
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1863] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1864] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[318] + 0.5)){
                    if (x_index[i] < (history[280] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1865] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1866] += x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[296] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1867] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1868] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[275] + 0.5)){
                    if (x_index[i] < (history[301] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1869] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[1870])){
                            history[1870] = screen_coor_x_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[326] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1871] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1872] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[318] + 0.5)){
                    if (x_index[i] < (history[326] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1873] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[1874])){
                            history[1874] = screen_coor_x_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[321] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1875] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[1876])){
                            history[1876] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[284] + 0.5)){
                    if (x_index[i] < (history[324] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1877] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[1878])){
                            history[1878] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[338] + 0.5)){
                    if (x_index[i] < (history[301] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1879] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1880] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1881] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[280] + 0.5)){
                    if (x_index[i] < (history[313] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1882] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[1883])){
                            history[1883] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[275] + 0.5)){
                    if (x_index[i] < (history[326] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1884] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[1885])){
                            history[1885] = screen_coor_y_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[276] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1886] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1887] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[286] + 0.5)){
                    if (x_index[i] < (history[288] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1888] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1889] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[273] + 0.5)){
                    if (x_index[i] < (history[323] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1890] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1891] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[293] + 0.5)){
                    if (x_index[i] < (history[323] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1892] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1893] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1894] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                    if (x_index[i] < (history[296] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1895] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1896] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1897] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[283] + 0.5)){
                    if (x_index[i] < (history[291] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1898] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1899] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1900] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[323] + 0.5)){
                    if (x_index[i] < (history[341] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1901] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1902] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[324] + 0.5)){
                    if (x_index[i] < (history[347] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1903] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1904] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[336] + 0.5)){
                    if (x_index[i] < (history[326] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1905] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1906] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[290] + 0.5)){
                    if (x_index[i] < (history[315] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[1907] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[1908])){
                            history[1908] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[283] + 0.5)){
                    if (x_index[i] < (history[330] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[1909] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[1910] += et_since_prev;
                        }
                    }
                }
                if (x_en[i] == 9){
                    if (x_index[i] > (history[300] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1911] += 1;
                        }
                        if (isnan(history[1912])){
                            history[1912] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 0){
                    if (x_index[i] > (history[295] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1913] += 1;
                        }
                        if (isnan(history[1914])){
                            history[1914] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 1){
                if (x_text_fqid_numerical[i] == 67){
                    if (x_index[i] > (history[379] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1915] += 1;
                        }
                        if (isnan(history[1916])){
                            history[1916] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                    if (x_index[i] > (history[432] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1917] += 1;
                        }
                        if (isnan(history[1918])){
                            history[1918] = x_et[i];
                        }
                    }
                }
                if (x_fqids[i] == 30){
                    if (x_index[i] > (history[396] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1919] += 1;
                        }
                        if (isnan(history[1920])){
                            history[1920] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 0){
                    if (x_index[i] > (history[365] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1921] += 1;
                        }
                        if (isnan(history[1922])){
                            history[1922] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[424] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[1923] += 1;
                        }
                        history[1924] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 125){
                    if (x_index[i] > (history[420] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1925] += 1;
                        }
                        if (isnan(history[1926])){
                            history[1926] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[350] + 0.5)){
                    if (x_index[i] < (history[367] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1927] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[1928])){
                            history[1928] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[403] + 0.5)){
                    if (x_index[i] < (history[370] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1929] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[1930])){
                            history[1930] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[405] + 0.5)){
                    if (x_index[i] < (history[388] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[1931] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[1932] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[396] + 0.5)){
                    if (x_index[i] < (history[401] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1933] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[1934])){
                            history[1934] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[369] + 0.5)){
                    if (x_index[i] < (history[414] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1935] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[1936])){
                            history[1936] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[424] + 0.5)){
                    if (x_index[i] < (history[375] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1937] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[1938])){
                            history[1938] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[438] + 0.5)){
                    if (x_index[i] < (history[414] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1939] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[1940] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[405] + 0.5)){
                    if (x_index[i] < (history[420] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1941] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[1942])){
                            history[1942] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[407] + 0.5)){
                    if (x_index[i] < (history[369] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[1943] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[1944])){
                            history[1944] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[396] + 0.5)){
                    if (x_index[i] < (history[397] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1945] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[1946] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[430] + 0.5)){
                    if (x_index[i] < (history[355] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1947] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[1948] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[354] + 0.5)){
                    if (x_index[i] < (history[384] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1949] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[1950] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[1951] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[432] + 0.5)){
                    if (x_index[i] < (history[370] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[1952] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[1953] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[369] + 0.5)){
                    if (x_index[i] < (history[414] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1954] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1955] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[377] + 0.5)){
                    if (x_index[i] < (history[357] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1956] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1957] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[380] + 0.5)){
                    if (x_index[i] < (history[433] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1958] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1959] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[374] + 0.5)){
                    if (x_index[i] < (history[418] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1960] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[1961])){
                            history[1961] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[396] + 0.5)){
                    if (x_index[i] < (history[386] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1962] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1963] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1964] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[432] + 0.5)){
                    if (x_index[i] < (history[367] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[1965] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1966] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[1967] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_en[i] == 1){
                    if (x_index[i] > (history[394] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1968] += 1;
                        }
                        if (isnan(history[1969])){
                            history[1969] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 5){
                    if (x_index[i] > (history[396] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1970] += 1;
                        }
                        if (isnan(history[1971])){
                            history[1971] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[413] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1972] += 1;
                        }
                        if (isnan(history[1973])){
                            history[1973] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[361] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1974] += 1;
                        }
                        if (isnan(history[1975])){
                            history[1975] = x_et[i];
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 7){
                    if (x_index[i] > (history[411] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1976] += 1;
                        }
                        if (isnan(history[1977])){
                            history[1977] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[437] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1978] += 1;
                        }
                        if (isnan(history[1979])){
                            history[1979] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 5){
                    if (x_index[i] > (history[411] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1980] += 1;
                        }
                        if (isnan(history[1981])){
                            history[1981] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[437] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1982] += 1;
                        }
                        if (isnan(history[1983])){
                            history[1983] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[369] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1984] += 1;
                        }
                        if (isnan(history[1985])){
                            history[1985] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[420] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1986] += 1;
                        }
                        if (isnan(history[1987])){
                            history[1987] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[361] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1988] += 1;
                        }
                        if (isnan(history[1989])){
                            history[1989] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[388] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1990] += 1;
                        }
                        if (isnan(history[1991])){
                            history[1991] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[425] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1992] += 1;
                        }
                        if (isnan(history[1993])){
                            history[1993] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 2){
                    if (x_index[i] > (history[424] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1994] += 1;
                        }
                        if (isnan(history[1995])){
                            history[1995] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 1){
                    if (x_index[i] > (history[394] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1996] += 1;
                        }
                        if (isnan(history[1997])){
                            history[1997] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[437] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[1998] += 1;
                        }
                        if (isnan(history[1999])){
                            history[1999] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 0){
                    if (x_index[i] > (history[411] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2000] += 1;
                        }
                        if (isnan(history[2001])){
                            history[2001] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[394] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2002] += 1;
                        }
                        if (isnan(history[2003])){
                            history[2003] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[437] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2004] += 1;
                        }
                        if (isnan(history[2005])){
                            history[2005] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 3){
                    if (x_index[i] > (history[396] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2006] += 1;
                        }
                        if (isnan(history[2007])){
                            history[2007] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[394] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2008] += 1;
                        }
                        if (isnan(history[2009])){
                            history[2009] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[424] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2010] += 1;
                        }
                        if (isnan(history[2011])){
                            history[2011] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[349] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2012] += 1;
                        }
                        if (isnan(history[2013])){
                            history[2013] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[361] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2014] += 1;
                        }
                        if (isnan(history[2015])){
                            history[2015] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 2){
                if (x_fqids[i] == 119){
                    if (x_index[i] > (history[464] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2016] += 1;
                        }
                        if (isnan(history[2017])){
                            history[2017] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[497] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2018] += 1;
                        }
                        history[2019] = x_index[i];
                    }
                    if (x_index[i] > (history[477] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2020] += 1;
                        }
                        if (isnan(history[2021])){
                            history[2021] = x_index[i];
                        }
                    }
                }
                if (x_en[i] == 7){
                    if (x_index[i] > (history[445] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2022] += 1;
                        }
                        history[2023] = x_et[i];
                    }
                }
                else if (x_en[i] == 8){
                    if (x_index[i] > (history[457] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2024] += 1;
                        }
                        history[2025] = x_index[i];
                    }
                    if (x_index[i] > (history[458] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2026] += 1;
                        }
                        history[2027] = x_index[i];
                    }
                }
                if (x_index[i] > (history[443] + 0.5)){
                    if (x_index[i] < (history[460] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2028] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2029])){
                            history[2029] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[474] + 0.5)){
                    if (x_index[i] < (history[445] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2030] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2031])){
                            history[2031] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[477] + 0.5)){
                    if (x_index[i] < (history[460] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2032] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2033] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[481] + 0.5)){
                    if (x_index[i] < (history[484] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2034] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2035])){
                            history[2035] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[477] + 0.5)){
                    if (x_index[i] < (history[462] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2036] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2037])){
                            history[2037] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[479] + 0.5)){
                    if (x_index[i] < (history[495] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2038] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2039] += screen_coor_y_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[497] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2040] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2041] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[464] + 0.5)){
                    if (x_index[i] < (history[498] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2042] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2043])){
                            history[2043] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[442] + 0.5)){
                    if (x_index[i] < (history[443] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2044] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[2045])){
                            history[2045] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[451] + 0.5)){
                    if (x_index[i] < (history[453] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2046] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2047] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2048] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[505] + 0.5)){
                    if (x_index[i] < (history[449] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2049] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] < history[2050])){
                            history[2050] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[465] + 0.5)){
                    if (x_index[i] < (history[483] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2051] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[2052])){
                            history[2052] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[494] + 0.5)){
                    if (x_index[i] < (history[451] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2053] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2054] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2055] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[476] + 0.5)){
                    if (x_index[i] < (history[455] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2056] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2057] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2058] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[509] + 0.5)){
                    if (x_index[i] < (history[483] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2059] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2060] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2061] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[483] + 0.5)){
                    if (x_index[i] < (history[510] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2062] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2063] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2064] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[467] + 0.5)){
                    if (x_index[i] < (history[462] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2065] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2066] += x_rc_x[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[488] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2067] += 1;
                        }
                        if (isnan(history[2068])){
                            history[2068] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[472] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2069] += 1;
                        }
                        history[2070] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 56){
                    if (x_index[i] > (history[468] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2071] += 1;
                        }
                        history[2072] = x_index[i];
                    }
                    if (x_index[i] > (history[477] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2073] += 1;
                        }
                        history[2074] = x_index[i];
                    }
                }
                if (x_n[i] == 1){
                    if (x_index[i] > (history[504] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2075] += 1;
                        }
                        if (isnan(history[2076])){
                            history[2076] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 2){
                    if (x_index[i] > (history[502] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2077] += 1;
                        }
                        if (isnan(history[2078])){
                            history[2078] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[492] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2079] += 1;
                        }
                        if (isnan(history[2080])){
                            history[2080] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[464] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2081] += 1;
                        }
                        if (isnan(history[2082])){
                            history[2082] = x_index[i];
                        }
                    }
                }
            } else if (level[i] == 3){
                if (x_en[i] == 4){
                    if (x_index[i] > (history[519] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2083] += 1;
                        }
                        history[2084] = x_et[i];
                    }
                }
                if (x_fqids[i] == 0){
                    if (x_index[i] > (history[545] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2085] += 1;
                        }
                        if (isnan(history[2086])){
                            history[2086] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 105){
                    if (x_index[i] > (history[547] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2087] += 1;
                        }
                        if (isnan(history[2088])){
                            history[2088] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 72){
                    if (x_index[i] > (history[515] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2089] += 1;
                        }
                        if (isnan(history[2090])){
                            history[2090] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 71){
                    if (x_index[i] > (history[551] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2091] += 1;
                        }
                        if (isnan(history[2092])){
                            history[2092] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[512] + 0.5)){
                    if (x_index[i] < (history[549] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2093] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2094])){
                            history[2094] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[551] + 0.5)){
                    if (x_index[i] < (history[556] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2095] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2096])){
                            history[2096] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[523] + 0.5)){
                    if (x_index[i] < (history[613] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2097] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2098])){
                            history[2098] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[561] + 0.5)){
                    if (x_index[i] < (history[529] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2099] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2100])){
                            history[2100] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[571] + 0.5)){
                    if (x_index[i] < (history[513] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2101] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2102])){
                            history[2102] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[615] + 0.5)){
                    if (x_index[i] < (history[592] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2103] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2104])){
                            history[2104] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[524] + 0.5)){
                    if (x_index[i] < (history[617] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2105] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2106])){
                            history[2106] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[577] + 0.5)){
                    if (x_index[i] < (history[533] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2107] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2108])){
                            history[2108] = x_rc_x[i];
                        }
                    }
                    if (x_index[i] < (history[579] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2109] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2110])){
                            history[2110] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[515] + 0.5)){
                    if (x_index[i] < (history[566] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2111] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2112] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2113] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[594] + 0.5)){
                    if (x_index[i] < (history[596] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2114] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2115] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2116] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[569] + 0.5)){
                    if (x_index[i] < (history[598] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2117] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2118] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2119] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[572] + 0.5)){
                    if (x_index[i] < (history[600] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2120] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2121] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2122] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[515] + 0.5)){
                    if (x_index[i] < (history[558] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2123] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2124])){
                            history[2124] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[536] + 0.5)){
                    if (x_index[i] < (history[534] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2125] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2126])){
                            history[2126] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[581] + 0.5)){
                    if (x_index[i] < (history[513] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2127] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2128])){
                            history[2128] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[606] + 0.5)){
                    if (x_index[i] < (history[512] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2129] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2130] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2131] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[571] + 0.5)){
                    if (x_index[i] < (history[569] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2132] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2133] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[588] + 0.5)){
                    if (x_index[i] < (history[568] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2134] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2135] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[572] + 0.5)){
                    if (x_index[i] < (history[568] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2136] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2137] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[561] + 0.5)){
                    if (x_index[i] < (history[515] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2138] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2139])){
                            history[2139] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[558] + 0.5)){
                    if (x_index[i] < (history[552] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2140] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2141])){
                            history[2141] = screen_coor_y_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[579] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2142] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2143])){
                            history[2143] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[586] + 0.5)){
                    if (x_index[i] < (history[564] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2144] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2145])){
                            history[2145] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[602] + 0.5)){
                    if (x_index[i] < (history[552] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2146] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2147])){
                            history[2147] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[588] + 0.5)){
                    if (x_index[i] < (history[572] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2148] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2149] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[559] + 0.5)){
                    if (x_index[i] < (history[582] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2150] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2151] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2152] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[610] + 0.5)){
                    if (x_index[i] < (history[584] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2153] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2154] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2155] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[571] + 0.5)){
                    if (x_index[i] < (history[534] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2156] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2157] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[515] + 0.5)){
                    if (x_index[i] < (history[566] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2158] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2159] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[556] + 0.5)){
                    if (x_index[i] < (history[519] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2160] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2161] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[604] + 0.5)){
                    if (x_index[i] < (history[569] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2162] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2163] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[540] + 0.5)){
                    if (x_index[i] < (history[615] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2164] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2165] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2166] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[541] + 0.5)){
                    if (x_index[i] < (history[518] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2167] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2168] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2169] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[574] + 0.5)){
                    if (x_index[i] < (history[590] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2170] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] < history[2171])){
                            history[2171] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[575] + 0.5)){
                    if (x_index[i] < (history[562] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2172] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2173] += x_index[i];
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2174] += pow(x_index[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[512] + 0.5)){
                    if (x_index[i] < (history[515] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2175] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2176] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2177] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[529] + 0.5)){
                    if (x_index[i] < (history[516] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2178] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2179] += x_hover_duration[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 23){
                    if (x_index[i] > (history[528] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2180] += 1;
                        }
                        if (isnan(history[2181])){
                            history[2181] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 97){
                    if (x_index[i] > (history[536] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2182] += 1;
                        }
                        if (isnan(history[2183])){
                            history[2183] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 38){
                    if (x_index[i] > (history[536] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2184] += 1;
                        }
                        if (isnan(history[2185])){
                            history[2185] = x_et[i];
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[551] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2186] += 1;
                        }
                        history[2187] = x_et[i];
                    }
                }
                if (x_n[i] == 2){
                    if (x_index[i] > (history[574] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2188] += 1;
                        }
                        if (isnan(history[2189])){
                            history[2189] = x_index[i];
                        }
                    }
                }
                else if (x_n[i] == 3){
                    if (x_index[i] > (history[523] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2190] += 1;
                        }
                        if (isnan(history[2191])){
                            history[2191] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[606] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2192] += 1;
                        }
                        if (isnan(history[2193])){
                            history[2193] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 1){
                    if (x_index[i] > (history[515] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2194] += 1;
                        }
                        if (isnan(history[2195])){
                            history[2195] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[615] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2196] += 1;
                        }
                        if (isnan(history[2197])){
                            history[2197] = x_index[i];
                        }
                    }
                }
            } else if (level[i] == 4){
                if (x_fqids[i] == 113){
                    if (x_index[i] > (history[619] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2198] += 1;
                        }
                        history[2199] = x_index[i];
                    }
                }
                if (x_index[i] > (history[620] + 0.5)){
                    if (x_index[i] < (history[634] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2200] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2201])){
                            history[2201] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[622] + 0.5)){
                    if (x_index[i] < (history[655] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2202] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2203] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2204] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[630] + 0.5)){
                    if (x_index[i] < (history[646] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2205] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2206] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[642] + 0.5)){
                    if (x_index[i] < (history[643] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2207] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[2208])){
                            history[2208] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[650] + 0.5)){
                    if (x_index[i] < (history[619] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2209] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2210])){
                            history[2210] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[623] + 0.5)){
                    if (x_index[i] < (history[625] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2211] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2212])){
                            history[2212] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[627] + 0.5)){
                    if (x_index[i] < (history[651] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2213] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2214])){
                            history[2214] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[623] + 0.5)){
                    if (x_index[i] < (history[658] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2215] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2216] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[636] + 0.5)){
                    if (x_index[i] < (history[638] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2217] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2218])){
                            history[2218] = screen_coor_y_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[627] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2219] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2220])){
                            history[2220] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[650] + 0.5)){
                    if (x_index[i] < (history[619] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2221] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2222])){
                            history[2222] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[645] + 0.5)){
                    if (x_index[i] < (history[642] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2223] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2224])){
                            history[2224] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[653] + 0.5)){
                    if (x_index[i] < (history[630] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2225] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2226] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[645] + 0.5)){
                    if (x_index[i] < (history[629] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2227] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2228] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[619] + 0.5)){
                    if (x_index[i] < (history[634] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2229] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2230] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2231] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[629] + 0.5)){
                    if (x_index[i] < (history[632] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2232] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2233] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2234] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[630] + 0.5)){
                    if (x_index[i] < (history[660] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2235] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2236] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2237] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[642] + 0.5)){
                    if (x_index[i] < (history[640] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2238] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2239] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[627] + 0.5)){
                    if (x_index[i] < (history[656] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2240] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2241] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[646] + 0.5)){
                    if (x_index[i] < (history[643] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2242] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2243] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[634] + 0.5)){
                    if (x_index[i] < (history[660] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2244] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[2245])){
                            history[2245] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[623] + 0.5)){
                    if (x_index[i] < (history[646] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2246] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2247] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2248] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 2){
                    if (x_index[i] > (history[645] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2249] += 1;
                        }
                        if (isnan(history[2250])){
                            history[2250] = x_et[i];
                        }
                    }
                }
            }
        }
    } else if (lg == 1){

        for (int i=0; i < n; i++){
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (level[i] == 5){
                if (x_en[i] == 2){
                    if (x_index[i] > (history[929] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2251] += 1;
                        }
                        history[2252] = x_index[i];
                    }
                }
                else if (x_en[i] == 1){
                    if (x_index[i] > (history[903] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2253] += 1;
                        }
                        history[2254] = x_index[i];
                    }
                    if (x_index[i] > (history[902] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2255] += 1;
                        }
                        history[2256] = x_et[i];
                    }
                    if (x_index[i] > (history[897] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2257] += 1;
                        }
                        if (isnan(history[2258])){
                            history[2258] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 5){
                    if (x_index[i] > (history[958] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2259] += 1;
                        }
                        if (isnan(history[2260])){
                            history[2260] = x_et[i];
                        }
                    }
                }
                if (x_fqids[i] == 121){
                    if (x_index[i] > (history[858] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2261] += 1;
                        }
                        if (isnan(history[2262])){
                            history[2262] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 113){
                    if (x_index[i] > (history[858] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2263] += 1;
                        }
                        if (isnan(history[2264])){
                            history[2264] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[951] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2265] += 1;
                        }
                        if (isnan(history[2266])){
                            history[2266] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[858] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2267] += 1;
                        }
                        history[2268] = x_et[i];
                    }
                    if (x_index[i] > (history[921] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2269] += 1;
                        }
                        if (isnan(history[2270])){
                            history[2270] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[936] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2271] += 1;
                        }
                        if (isnan(history[2272])){
                            history[2272] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 43){
                    if (x_index[i] > (history[913] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2273] += 1;
                        }
                        if (isnan(history[2274])){
                            history[2274] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 127){
                    if (x_index[i] > (history[903] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2275] += 1;
                        }
                        if (isnan(history[2276])){
                            history[2276] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 0){
                    if (x_index[i] > (history[878] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2277] += 1;
                        }
                        if (isnan(history[2278])){
                            history[2278] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[897] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2279] += 1;
                        }
                        if (isnan(history[2280])){
                            history[2280] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[853] + 0.5)){
                    if (x_index[i] < (history[880] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2281] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2282])){
                            history[2282] = et_since_prev;
                        }
                    }
                    if (x_index[i] < (history[908] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2283] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2284] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2285] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[931] + 0.5)){
                    if (x_index[i] < (history[882] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2286] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2287])){
                            history[2287] = et_since_prev;
                        }
                    }
                    if (x_index[i] < (history[890] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2288] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[2289])){
                            history[2289] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[902] + 0.5)){
                    if (x_index[i] < (history[908] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2290] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2291] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[880] + 0.5)){
                    if (x_index[i] < (history[869] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2292] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[2293])){
                            history[2293] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[911] + 0.5)){
                    if (x_index[i] < (history[888] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2294] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[2295])){
                            history[2295] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[884] + 0.5)){
                    if (x_index[i] < (history[914] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2296] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2297] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2298] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[903] + 0.5)){
                    if (x_index[i] < (history[890] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2299] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2300] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[884] + 0.5)){
                    if (x_index[i] < (history[887] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2301] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2302])){
                            history[2302] = x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[952] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2303] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2304])){
                            history[2304] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[954] + 0.5)){
                    if (x_index[i] < (history[863] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2305] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2306] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2307] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[868] + 0.5)){
                    if (x_index[i] < (history[947] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2308] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2309] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[960] + 0.5)){
                    if (x_index[i] < (history[934] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2310] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2311])){
                            history[2311] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[854] + 0.5)){
                    if (x_index[i] < (history[891] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2312] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2313])){
                            history[2313] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[853] + 0.5)){
                    if (x_index[i] < (history[864] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2314] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2315] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[887] + 0.5)){
                    if (x_index[i] < (history[934] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2316] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2317] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[871] + 0.5)){
                    if (x_index[i] < (history[872] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2318] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2319])){
                            history[2319] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[874] + 0.5)){
                    if (x_index[i] < (history[937] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2320] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2321])){
                            history[2321] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[941] + 0.5)){
                    if (x_index[i] < (history[914] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2322] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2323])){
                            history[2323] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[963] + 0.5)){
                    if (x_index[i] < (history[869] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2324] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2325])){
                            history[2325] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[869] + 0.5)){
                    if (x_index[i] < (history[918] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2326] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2327])){
                            history[2327] = x_rc_x[i];
                        }
                    }
                    if (x_index[i] < (history[872] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2328] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2329] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2330] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[922] + 0.5)){
                    if (x_index[i] < (history[872] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2331] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2332])){
                            history[2332] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[952] + 0.5)){
                    if (x_index[i] < (history[872] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2333] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2334])){
                            history[2334] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[945] + 0.5)){
                    if (x_index[i] < (history[919] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2335] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2336])){
                            history[2336] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[928] + 0.5)){
                    if (x_index[i] < (history[944] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2337] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2338] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[859] + 0.5)){
                    if (x_index[i] < (history[934] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2339] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2340])){
                            history[2340] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[893] + 0.5)){
                    if (x_index[i] < (history[895] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2341] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2342])){
                            history[2342] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[891] + 0.5)){
                    if (x_index[i] < (history[961] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2343] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2344])){
                            history[2344] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[954] + 0.5)){
                    if (x_index[i] < (history[949] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2345] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2346] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2347] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[937] + 0.5)){
                    if (x_index[i] < (history[872] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2348] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2349] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2350] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[884] + 0.5)){
                    if (x_index[i] < (history[942] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2351] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2352] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[945] + 0.5)){
                    if (x_index[i] < (history[961] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2353] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2354] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[884] + 0.5)){
                    if (x_index[i] < (history[931] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2355] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2356])){
                            history[2356] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[893] + 0.5)){
                    if (x_index[i] < (history[898] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2357] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2358])){
                            history[2358] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[910] + 0.5)){
                    if (x_index[i] < (history[866] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2359] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2360] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[890] + 0.5)){
                    if (x_index[i] < (history[922] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2361] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2362])){
                            history[2362] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[965] + 0.5)){
                    if (x_index[i] < (history[893] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2363] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2364])){
                            history[2364] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[926] + 0.5)){
                    if (x_index[i] < (history[913] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2365] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2366] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2367] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[903] + 0.5)){
                    if (x_index[i] < (history[932] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2368] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2369] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2370] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[954] + 0.5)){
                    if (x_index[i] < (history[863] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2371] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2372] += x_index[i];
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2373] += pow(x_index[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[853] + 0.5)){
                    if (x_index[i] < (history[891] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2374] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2375] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2376] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[908] + 0.5)){
                    if (x_index[i] < (history[863] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2377] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2378] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2379] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[947] + 0.5)){
                    if (x_index[i] < (history[885] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2380] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2381] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2382] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[967] + 0.5)){
                    if (x_index[i] < (history[880] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2383] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2384] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2385] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[921] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2386] += 1;
                        }
                        if (isnan(history[2387])){
                            history[2387] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 0){
                    if (x_index[i] > (history[926] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2388] += 1;
                        }
                        history[2389] = x_index[i];
                    }
                    if (x_index[i] > (history[949] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2390] += 1;
                        }
                        history[2391] = x_index[i];
                    }
                    if (x_index[i] > (history[853] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2392] += 1;
                        }
                        history[2393] = x_et[i];
                    }
                    if (x_index[i] > (history[913] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2394] += 1;
                        }
                        if (isnan(history[2395])){
                            history[2395] = x_et[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 50){
                    if (x_index[i] > (history[897] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2396] += 1;
                        }
                        if (isnan(history[2397])){
                            history[2397] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[878] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2398] += 1;
                        }
                        if (isnan(history[2399])){
                            history[2399] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                    if (x_index[i] > (history[913] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2400] += 1;
                        }
                        if (isnan(history[2401])){
                            history[2401] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 6){
                if (x_text_fqid_numerical[i] == 45){
                    if (x_index[i] > (history[1088] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2402] += 1;
                        }
                        if (isnan(history[2403])){
                            history[2403] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 75){
                    if (x_index[i] > (history[1035] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2404] += 1;
                        }
                        if (isnan(history[2405])){
                            history[2405] = x_et[i];
                        }
                    }
                }
                if (x_fqids[i] == 66){
                    if (x_index[i] > (history[1043] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2406] += 1;
                        }
                        if (isnan(history[2407])){
                            history[2407] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 101){
                    if (x_index[i] > (history[1007] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2408] += 1;
                        }
                        if (isnan(history[2409])){
                            history[2409] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 1){
                    if (x_index[i] > (history[1062] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2410] += 1;
                        }
                        if (isnan(history[2411])){
                            history[2411] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 107){
                    if (x_index[i] > (history[1055] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2412] += 1;
                        }
                        history[2413] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 8){
                    if (x_index[i] > (history[1047] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2414] += 1;
                        }
                        if (isnan(history[2415])){
                            history[2415] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 110){
                    if (x_index[i] > (history[986] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2416] += 1;
                        }
                        history[2417] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 102){
                    if (x_index[i] > (history[1084] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2418] += 1;
                        }
                        history[2419] = x_index[i];
                    }
                }
                if (x_index[i] > (history[969] + 0.5)){
                    if (x_index[i] < (history[1009] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2420] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2421])){
                            history[2421] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1024] + 0.5)){
                    if (x_index[i] < (history[1026] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2422] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2423] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2424] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[990] + 0.5)){
                    if (x_index[i] < (history[992] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2425] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2426] += et_since_prev;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2427] += pow(et_since_prev, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1049] + 0.5)){
                    if (x_index[i] < (history[1009] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2428] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2429])){
                            history[2429] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1070] + 0.5)){
                    if (x_index[i] < (history[976] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2430] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2431] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1009] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2432] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2433] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[973] + 0.5)){
                    if (x_index[i] < (history[1082] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2434] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2435] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[977] + 0.5)){
                    if (x_index[i] < (history[1010] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2436] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2437] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1060] + 0.5)){
                    if (x_index[i] < (history[1012] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2438] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[2439])){
                            history[2439] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[995] + 0.5)){
                    if (x_index[i] < (history[1010] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2440] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2441] += x_index[i];
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2442] += pow(x_index[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1081] + 0.5)){
                    if (x_index[i] < (history[1029] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2443] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2444] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1062] + 0.5)){
                    if (x_index[i] < (history[1066] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2445] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2446])){
                            history[2446] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1016] + 0.5)){
                    if (x_index[i] < (history[1012] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2447] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2448])){
                            history[2448] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1079] + 0.5)){
                    if (x_index[i] < (history[1021] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2449] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2450])){
                            history[2450] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1053] + 0.5)){
                    if (x_index[i] < (history[974] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2451] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2452] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1051] + 0.5)){
                    if (x_index[i] < (history[1014] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2453] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2454])){
                            history[2454] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[971] + 0.5)){
                    if (x_index[i] < (history[1068] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2455] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2456])){
                            history[2456] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[1017] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2457] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2458] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1056] + 0.5)){
                    if (x_index[i] < (history[1062] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2459] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2460] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1023] + 0.5)){
                    if (x_index[i] < (history[1009] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2461] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2462] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2463] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1081] + 0.5)){
                    if (x_index[i] < (history[1028] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2464] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2465] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1053] + 0.5)){
                    if (x_index[i] < (history[974] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2466] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2467])){
                            history[2467] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[994] + 0.5)){
                    if (x_index[i] < (history[1014] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2468] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2469] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1072] + 0.5)){
                    if (x_index[i] < (history[979] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2470] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2471] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[982] + 0.5)){
                    if (x_index[i] < (history[1077] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2472] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2473] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[984] + 0.5)){
                    if (x_index[i] < (history[986] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2474] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2475] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1073] + 0.5)){
                    if (x_index[i] < (history[1014] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2476] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2477] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 12){
                    if (x_index[i] > (history[999] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2478] += 1;
                        }
                        if (isnan(history[2479])){
                            history[2479] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[1016] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2480] += 1;
                        }
                        history[2481] = x_et[i];
                    }
                }
                if (x_en[i] == 2){
                    if (x_index[i] > (history[1039] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2482] += 1;
                        }
                        if (isnan(history[2483])){
                            history[2483] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 4){
                    if (x_index[i] > (history[980] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2484] += 1;
                        }
                        if (isnan(history[2485])){
                            history[2485] = x_index[i];
                        }
                    }
                }
                else if (x_en[i] == 8){
                    if (x_index[i] > (history[1003] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2486] += 1;
                        }
                        if (isnan(history[2487])){
                            history[2487] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 10){
                    if (x_index[i] > (history[1062] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2488] += 1;
                        }
                        if (isnan(history[2489])){
                            history[2489] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 3){
                    if (x_index[i] > (history[1072] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2490] += 1;
                        }
                        if (isnan(history[2491])){
                            history[2491] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 5){
                    if (x_index[i] > (history[1034] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2492] += 1;
                        }
                        if (isnan(history[2493])){
                            history[2493] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 0){
                    if (x_index[i] > (history[999] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2494] += 1;
                        }
                        if (isnan(history[2495])){
                            history[2495] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1084] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2496] += 1;
                        }
                        if (isnan(history[2497])){
                            history[2497] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1029] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2498] += 1;
                        }
                        if (isnan(history[2499])){
                            history[2499] = x_index[i];
                        }
                    }
                }
            } else if (level[i] == 7){
                if (x_fqids[i] == 18){
                    if (x_index[i] > (history[1221] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2500] += 1;
                        }
                        if (isnan(history[2501])){
                            history[2501] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1222] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2502] += 1;
                        }
                        if (isnan(history[2503])){
                            history[2503] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1233] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2504] += 1;
                        }
                        if (isnan(history[2505])){
                            history[2505] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2506] += 1;
                        }
                        if (isnan(history[2507])){
                            history[2507] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1171] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2508] += 1;
                        }
                        if (isnan(history[2509])){
                            history[2509] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1094] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2510] += 1;
                        }
                        if (isnan(history[2511])){
                            history[2511] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1173] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2512] += 1;
                        }
                        if (isnan(history[2513])){
                            history[2513] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2514] += 1;
                        }
                        if (isnan(history[2515])){
                            history[2515] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 14){
                    if (x_index[i] > (history[1121] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2516] += 1;
                        }
                        if (isnan(history[2517])){
                            history[2517] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 128){
                    if (x_index[i] > (history[1121] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2518] += 1;
                        }
                        history[2519] = x_index[i];
                    }
                    if (x_index[i] > (history[1153] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2520] += 1;
                        }
                        history[2521] = x_index[i];
                    }
                    if (x_index[i] > (history[1232] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2522] += 1;
                        }
                        if (isnan(history[2523])){
                            history[2523] = x_et[i];
                        }
                        history[2524] = x_et[i];
                    }
                    if (x_index[i] > (history[1162] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2525] += 1;
                        }
                        if (isnan(history[2526])){
                            history[2526] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1178] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2527] += 1;
                        }
                        if (isnan(history[2528])){
                            history[2528] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 17){
                    if (x_index[i] > (history[1138] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2529] += 1;
                        }
                        history[2530] = x_index[i];
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2531] += 1;
                        }
                        if (isnan(history[2532])){
                            history[2532] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 15){
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2533] += 1;
                        }
                        if (isnan(history[2534])){
                            history[2534] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1224] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2535] += 1;
                        }
                        history[2536] = x_et[i];
                    }
                    if (x_index[i] > (history[1099] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2537] += 1;
                        }
                        history[2538] = x_et[i];
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2539] += 1;
                        }
                        if (isnan(history[2540])){
                            history[2540] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 101){
                    if (x_index[i] > (history[1216] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2541] += 1;
                        }
                        history[2542] = x_et[i];
                    }
                    if (x_index[i] > (history[1190] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2543] += 1;
                        }
                        history[2544] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 0){
                    if (x_index[i] > (history[1202] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2545] += 1;
                        }
                        if (isnan(history[2546])){
                            history[2546] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 43){
                    if (x_index[i] > (history[1206] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2547] += 1;
                        }
                        if (isnan(history[2548])){
                            history[2548] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 16){
                    if (x_index[i] > (history[1110] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2549] += 1;
                        }
                        if (isnan(history[2550])){
                            history[2550] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 114){
                    if (x_index[i] > (history[1162] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2551] += 1;
                        }
                        if (isnan(history[2552])){
                            history[2552] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 2){
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2553] += 1;
                        }
                        if (isnan(history[2554])){
                            history[2554] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1232] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2555] += 1;
                        }
                        if (isnan(history[2556])){
                            history[2556] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1240] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2557] += 1;
                        }
                        if (isnan(history[2558])){
                            history[2558] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1158] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2559] += 1;
                        }
                        if (isnan(history[2560])){
                            history[2560] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 0){
                    if (x_index[i] > (history[1110] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2561] += 1;
                        }
                        if (isnan(history[2562])){
                            history[2562] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1136] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2563] += 1;
                        }
                        if (isnan(history[2564])){
                            history[2564] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1178] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2565] += 1;
                        }
                        if (isnan(history[2566])){
                            history[2566] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1153] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2567] += 1;
                        }
                        if (isnan(history[2568])){
                            history[2568] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 1){
                    if (x_index[i] > (history[1232] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2569] += 1;
                        }
                        history[2570] = x_et[i];
                    }
                }
                if (x_index[i] > (history[1094] + 0.5)){
                    if (x_index[i] < (history[1155] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2571] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2572])){
                            history[2572] = et_since_prev;
                        }
                    }
                    if (x_index[i] < (history[1100] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2573] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2574] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1170] + 0.5)){
                    if (x_index[i] < (history[1191] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2575] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2576])){
                            history[2576] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1188] + 0.5)){
                    if (x_index[i] < (history[1217] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2577] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2578] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1099] + 0.5)){
                    if (x_index[i] < (history[1208] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2579] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2580])){
                            history[2580] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1157] + 0.5)){
                    if (x_index[i] < (history[1211] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2581] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2582])){
                            history[2582] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1170] + 0.5)){
                    if (x_index[i] < (history[1214] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2583] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2584])){
                            history[2584] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1105] + 0.5)){
                    if (x_index[i] < (history[1108] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2585] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2586])){
                            history[2586] = x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1107] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2587] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2588] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1216] + 0.5)){
                    if (x_index[i] < (history[1108] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2589] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2590] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1173] + 0.5)){
                    if (x_index[i] < (history[1108] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2591] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2592] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1209] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2593] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2594] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1129] + 0.5)){
                    if (x_index[i] < (history[1200] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2595] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2596] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2597] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1115] + 0.5)){
                    if (x_index[i] < (history[1208] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2598] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2599] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2600] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1162] + 0.5)){
                    if (x_index[i] < (history[1199] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2601] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2602] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2603] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1134] + 0.5)){
                    if (x_index[i] < (history[1209] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2604] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2605] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2606] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1232] + 0.5)){
                    if (x_index[i] < (history[1130] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2607] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2608] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1217] + 0.5)){
                    if (x_index[i] < (history[1208] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2609] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2610] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1171] + 0.5)){
                    if (x_index[i] < (history[1208] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2611] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2612] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1099] + 0.5)){
                    if (x_index[i] < (history[1110] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2613] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2614])){
                            history[2614] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1116] + 0.5)){
                    if (x_index[i] < (history[1120] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2615] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2616] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1145] + 0.5)){
                    if (x_index[i] < (history[1222] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2617] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2618] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1136] + 0.5)){
                    if (x_index[i] < (history[1202] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2619] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2620] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1162] + 0.5)){
                    if (x_index[i] < (history[1115] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2621] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2622])){
                            history[2622] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[1217] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2623] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2624])){
                            history[2624] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1173] + 0.5)){
                    if (x_index[i] < (history[1111] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2625] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2626])){
                            history[2626] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1214] + 0.5)){
                    if (x_index[i] < (history[1100] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2627] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2628])){
                            history[2628] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1118] + 0.5)){
                    if (x_index[i] < (history[1197] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2629] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2630])){
                            history[2630] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[1120] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2631] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2632])){
                            history[2632] = x_rc_y[i];
                        }
                    }
                    if (x_index[i] < (history[1222] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2633] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2634])){
                            history[2634] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1116] + 0.5)){
                    if (x_index[i] < (history[1107] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2635] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2636])){
                            history[2636] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1174] + 0.5)){
                    if (x_index[i] < (history[1214] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2637] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2638])){
                            history[2638] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1127] + 0.5)){
                    if (x_index[i] < (history[1183] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2639] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2640] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1216] + 0.5)){
                    if (x_index[i] < (history[1183] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2641] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2642])){
                            history[2642] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1095] + 0.5)){
                    if (x_index[i] < (history[1225] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2643] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[2644])){
                            history[2644] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1229] + 0.5)){
                    if (x_index[i] < (history[1136] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2645] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2646] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2647] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1118] + 0.5)){
                    if (x_index[i] < (history[1155] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2648] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2649])){
                            history[2649] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1174] + 0.5)){
                    if (x_index[i] < (history[1120] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2650] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2651])){
                            history[2651] = screen_coor_x_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[1179] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2652] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2653])){
                            history[2653] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1110] + 0.5)){
                    if (x_index[i] < (history[1200] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2654] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2655] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1171] + 0.5)){
                    if (x_index[i] < (history[1107] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2656] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2657] += screen_coor_x_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[1222] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2658] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2659] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1099] + 0.5)){
                    if (x_index[i] < (history[1108] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2660] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[2661])){
                            history[2661] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1167] + 0.5)){
                    if (x_index[i] < (history[1130] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2662] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2663] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2664] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1173] + 0.5)){
                    if (x_index[i] < (history[1163] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2665] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2666] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2667] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1196] + 0.5)){
                    if (x_index[i] < (history[1130] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2668] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2669] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2670] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1230] + 0.5)){
                    if (x_index[i] < (history[1138] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2671] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2672] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2673] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1186] + 0.5)){
                    if (x_index[i] < (history[1197] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2674] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2675] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1222] + 0.5)){
                    if (x_index[i] < (history[1104] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2676] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2677])){
                            history[2677] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1125] + 0.5)){
                    if (x_index[i] < (history[1225] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2678] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2679])){
                            history[2679] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1168] + 0.5)){
                    if (x_index[i] < (history[1209] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2680] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[2681])){
                            history[2681] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1185] + 0.5)){
                    if (x_index[i] < (history[1209] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2682] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2683] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2684] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1127] + 0.5)){
                    if (x_index[i] < (history[1143] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2685] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2686] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2687] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1108] + 0.5)){
                    if (x_index[i] < (history[1214] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2688] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2689] += x_index[i];
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[1153] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2690] += 1;
                        }
                        history[2691] = x_et[i];
                    }
                }
                if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2692] += 1;
                        }
                        history[2693] = x_index[i];
                    }
                    if (x_index[i] > (history[1233] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2694] += 1;
                        }
                        if (isnan(history[2695])){
                            history[2695] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 93){
                    if (x_index[i] > (history[1213] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2696] += 1;
                        }
                        history[2697] = x_index[i];
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2698] += 1;
                        }
                        history[2699] = x_et[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 95){
                    if (x_index[i] > (history[1221] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2700] += 1;
                        }
                        if (isnan(history[2701])){
                            history[2701] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1190] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2702] += 1;
                        }
                        if (isnan(history[2703])){
                            history[2703] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1191] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2704] += 1;
                        }
                        history[2705] = x_et[i];
                    }
                }
                if (x_en[i] == 6){
                    if (x_index[i] > (history[1232] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2706] += 1;
                        }
                        history[2707] = x_index[i];
                    }
                    if (x_index[i] > (history[1138] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2708] += 1;
                        }
                        if (isnan(history[2709])){
                            history[2709] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1107] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2710] += 1;
                        }
                        history[2711] = x_index[i];
                    }
                }
                else if (x_en[i] == 9){
                    if (x_index[i] > (history[1145] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2712] += 1;
                        }
                        if (isnan(history[2713])){
                            history[2713] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 8){
                    if (x_index[i] > (history[1099] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2714] += 1;
                        }
                        if (isnan(history[2715])){
                            history[2715] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1230] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2716] += 1;
                        }
                        if (isnan(history[2717])){
                            history[2717] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1139] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2718] += 1;
                        }
                        if (isnan(history[2719])){
                            history[2719] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1136] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2720] += 1;
                        }
                        if (isnan(history[2721])){
                            history[2721] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1110] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2722] += 1;
                        }
                        if (isnan(history[2723])){
                            history[2723] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 10){
                    if (x_index[i] > (history[1155] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2724] += 1;
                        }
                        if (isnan(history[2725])){
                            history[2725] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1121] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2726] += 1;
                        }
                        history[2727] = x_index[i];
                    }
                    if (x_index[i] > (history[1136] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2728] += 1;
                        }
                        if (isnan(history[2729])){
                            history[2729] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1121] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2730] += 1;
                        }
                        if (isnan(history[2731])){
                            history[2731] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 2){
                    if (x_index[i] > (history[1120] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2732] += 1;
                        }
                        history[2733] = x_index[i];
                    }
                    if (x_index[i] > (history[1152] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2734] += 1;
                        }
                        if (isnan(history[2735])){
                            history[2735] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 7){
                    if (x_index[i] > (history[1152] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2736] += 1;
                        }
                        if (isnan(history[2737])){
                            history[2737] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 4){
                    if (x_index[i] > (history[1240] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2738] += 1;
                        }
                        if (isnan(history[2739])){
                            history[2739] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 3){
                    if (x_index[i] > (history[1129] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2740] += 1;
                        }
                        if (isnan(history[2741])){
                            history[2741] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 8){
                if (x_fqids[i] == 65){
                    if (x_index[i] > (history[1276] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2742] += 1;
                        }
                        if (isnan(history[2743])){
                            history[2743] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[1242] + 0.5)){
                    if (x_index[i] < (history[1244] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2744] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2745])){
                            history[2745] = x_rc_x[i];
                        }
                    }
                    if (x_index[i] < (history[1281] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2746] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2747] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1260] + 0.5)){
                    if (x_index[i] < (history[1274] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2748] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2749])){
                            history[2749] = x_rc_x[i];
                        }
                    }
                    if (x_index[i] < (history[1284] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2750] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2751] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1290] + 0.5)){
                    if (x_index[i] < (history[1291] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2752] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2753] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1293] + 0.5)){
                    if (x_index[i] < (history[1291] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2754] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2755] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2756] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1251] + 0.5)){
                    if (x_index[i] < (history[1245] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2757] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2758] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1244] + 0.5)){
                    if (x_index[i] < (history[1263] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2759] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2760])){
                            history[2760] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1251] + 0.5)){
                    if (x_index[i] < (history[1268] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2761] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2762] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1267] + 0.5)){
                    if (x_index[i] < (history[1281] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2763] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2764] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1283] + 0.5)){
                    if (x_index[i] < (history[1260] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2765] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2766])){
                            history[2766] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1259] + 0.5)){
                    if (x_index[i] < (history[1265] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2767] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2768])){
                            history[2768] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1260] + 0.5)){
                    if (x_index[i] < (history[1262] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2769] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 < history[2770])){
                            history[2770] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1253] + 0.5)){
                    if (x_index[i] < (history[1290] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2771] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2772] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1288] + 0.5)){
                    if (x_index[i] < (history[1295] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2773] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2774] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1249] + 0.5)){
                    if (x_index[i] < (history[1277] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2775] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2776] += x_hover_duration[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 94){
                    if (x_index[i] > (history[1257] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2777] += 1;
                        }
                        if (isnan(history[2778])){
                            history[2778] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 1){
                    if (x_index[i] > (history[1283] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2779] += 1;
                        }
                        if (isnan(history[2780])){
                            history[2780] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 0){
                    if (x_index[i] > (history[1244] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2781] += 1;
                        }
                        if (isnan(history[2782])){
                            history[2782] = x_et[i];
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 14){
                    if (x_index[i] > (history[1272] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2783] += 1;
                        }
                        if (isnan(history[2784])){
                            history[2784] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1299] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2785] += 1;
                        }
                        if (isnan(history[2786])){
                            history[2786] = x_et[i];
                        }
                    }
                }
                if (x_en[i] == 6){
                    if (x_index[i] > (history[1276] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2787] += 1;
                        }
                        if (isnan(history[2788])){
                            history[2788] = x_et[i];
                        }
                        history[2789] = x_et[i];
                    }
                }
            } else if (level[i] == 9){
                if (x_fqids[i] == 0){
                    if (x_index[i] > (history[1330] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2790] += 1;
                        }
                        history[2791] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 73){
                    if (x_index[i] > (history[1345] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2792] += 1;
                        }
                        history[2793] = x_index[i];
                    }
                    if (x_index[i] > (history[1313] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2794] += 1;
                        }
                        history[2795] = x_index[i];
                    }
                    if (x_index[i] > (history[1335] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2796] += 1;
                        }
                        if (isnan(history[2797])){
                            history[2797] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 79){
                    if (x_index[i] > (history[1329] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2798] += 1;
                        }
                        if (isnan(history[2799])){
                            history[2799] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 75){
                    if (x_index[i] > (history[1370] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2800] += 1;
                        }
                        history[2801] = x_et[i];
                    }
                }
                if (x_en[i] == 8){
                    if (x_index[i] > (history[1346] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2802] += 1;
                        }
                        history[2803] = x_index[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (x_index[i] > (history[1382] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2804] += 1;
                        }
                        if (isnan(history[2805])){
                            history[2805] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 10){
                    if (x_index[i] > (history[1305] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2806] += 1;
                        }
                        if (isnan(history[2807])){
                            history[2807] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1369] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2808] += 1;
                        }
                        history[2809] = x_et[i];
                    }
                    if (x_index[i] > (history[1354] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2810] += 1;
                        }
                        if (isnan(history[2811])){
                            history[2811] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[1303] + 0.5)){
                    if (x_index[i] < (history[1337] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2812] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2813])){
                            history[2813] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1384] + 0.5)){
                    if (x_index[i] < (history[1330] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2814] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev < history[2815])){
                            history[2815] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1340] + 0.5)){
                    if (x_index[i] < (history[1345] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2816] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2817])){
                            history[2817] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1305] + 0.5)){
                    if (x_index[i] < (history[1310] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2818] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2819])){
                            history[2819] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1359] + 0.5)){
                    if (x_index[i] < (history[1369] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2820] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2821])){
                            history[2821] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1376] + 0.5)){
                    if (x_index[i] < (history[1313] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2822] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2823])){
                            history[2823] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1362] + 0.5)){
                    if (x_index[i] < (history[1313] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2824] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2825])){
                            history[2825] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1375] + 0.5)){
                    if (x_index[i] < (history[1306] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2826] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2827] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1351] + 0.5)){
                    if (x_index[i] < (history[1353] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2828] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2829] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2830] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1324] + 0.5)){
                    if (x_index[i] < (history[1310] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2831] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2832] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2833] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1361] + 0.5)){
                    if (x_index[i] < (history[1364] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2834] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2835] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2836] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1315] + 0.5)){
                    if (x_index[i] < (history[1376] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2837] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[2838])){
                            history[2838] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1316] + 0.5)){
                    if (x_index[i] < (history[1338] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2839] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[2840])){
                            history[2840] = x_index[i];
                        }
                    }
                    if (x_index[i] < (history[1318] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2841] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[2842])){
                            history[2842] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1375] + 0.5)){
                    if (x_index[i] < (history[1312] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2843] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[2844] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1303] + 0.5)){
                    if (x_index[i] < (history[1320] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2845] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[2846])){
                            history[2846] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1348] + 0.5)){
                    if (x_index[i] < (history[1327] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2847] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2848] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1324] + 0.5)){
                    if (x_index[i] < (history[1389] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2849] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2850])){
                            history[2850] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1306] + 0.5)){
                    if (x_index[i] < (history[1367] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2851] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2852] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2853] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1329] + 0.5)){
                    if (x_index[i] < (history[1393] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2854] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2855] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1306] + 0.5)){
                    if (x_index[i] < (history[1322] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2856] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2857])){
                            history[2857] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1335] + 0.5)){
                    if (x_index[i] < (history[1341] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2858] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2859] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1364] + 0.5)){
                    if (x_index[i] < (history[1338] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2860] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2861])){
                            history[2861] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1325] + 0.5)){
                    if (x_index[i] < (history[1337] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2862] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[2863])){
                            history[2863] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1348] + 0.5)){
                    if (x_index[i] < (history[1365] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2864] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2865] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1361] + 0.5)){
                    if (x_index[i] < (history[1341] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2866] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2867] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1362] + 0.5)){
                    if (x_index[i] < (history[1376] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2868] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2869])){
                            history[2869] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1346] + 0.5)){
                    if (x_index[i] < (history[1341] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2870] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2871] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[1388] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2872] += 1;
                        }
                        if (isnan(history[2873])){
                            history[2873] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 106){
                    if (x_index[i] > (history[1376] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2874] += 1;
                        }
                        history[2875] = x_index[i];
                    }
                    if (x_index[i] > (history[1384] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2876] += 1;
                        }
                        if (isnan(history[2877])){
                            history[2877] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1376] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2878] += 1;
                        }
                        history[2879] = x_et[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 16){
                    if (x_index[i] > (history[1353] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2880] += 1;
                        }
                        if (isnan(history[2881])){
                            history[2881] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 17){
                    if (x_index[i] > (history[1370] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2882] += 1;
                        }
                        if (isnan(history[2883])){
                            history[2883] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 0){
                    if (x_index[i] > (history[1349] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2884] += 1;
                        }
                        if (isnan(history[2885])){
                            history[2885] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1340] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2886] += 1;
                        }
                        if (isnan(history[2887])){
                            history[2887] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 10){
                if (x_fqids[i] == 128){
                    if (x_index[i] > (history[1460] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2888] += 1;
                        }
                        if (isnan(history[2889])){
                            history[2889] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1444] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2890] += 1;
                        }
                        history[2891] = x_et[i];
                    }
                }
                else if (x_fqids[i] == 73){
                    if (x_index[i] > (history[1416] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2892] += 1;
                        }
                        if (isnan(history[2893])){
                            history[2893] = x_et[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 111){
                    if (x_index[i] > (history[1451] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2894] += 1;
                        }
                        if (isnan(history[2895])){
                            history[2895] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1424] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2896] += 1;
                        }
                        if (isnan(history[2897])){
                            history[2897] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[1395] + 0.5)){
                    if (x_index[i] < (history[1418] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2898] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[2899])){
                            history[2899] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1401] + 0.5)){
                    if (x_index[i] < (history[1406] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2900] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2901] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2902] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1467] + 0.5)){
                    if (x_index[i] < (history[1409] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[2903] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2904] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[2905] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1398] + 0.5)){
                    if (x_index[i] < (history[1420] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2906] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2907] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1399] + 0.5)){
                    if (x_index[i] < (history[1439] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2908] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2909] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1411] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2910] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2911] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1476] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2912] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2913] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1402] + 0.5)){
                    if (x_index[i] < (history[1422] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2914] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2915] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1467] + 0.5)){
                    if (x_index[i] < (history[1425] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2916] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2917] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1441] + 0.5)){
                    if (x_index[i] < (history[1412] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2918] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2919] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2920] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1466] + 0.5)){
                    if (x_index[i] < (history[1408] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[2921] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[2922] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1404] + 0.5)){
                    if (x_index[i] < (history[1472] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2923] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2924] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1438] + 0.5)){
                    if (x_index[i] < (history[1402] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2925] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[2926])){
                            history[2926] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1408] + 0.5)){
                    if (x_index[i] < (history[1430] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2927] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2928] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2929] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1471] + 0.5)){
                    if (x_index[i] < (history[1396] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2930] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2931] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2932] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1467] + 0.5)){
                    if (x_index[i] < (history[1445] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2933] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2934] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2935] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1429] + 0.5)){
                    if (x_index[i] < (history[1442] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2936] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2937] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1452] + 0.5)){
                    if (x_index[i] < (history[1456] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[2938] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[2939] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1395] + 0.5)){
                    if (x_index[i] < (history[1396] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2940] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[2941])){
                            history[2941] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1449] + 0.5)){
                    if (x_index[i] < (history[1439] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[2942] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[2943] += x_rc_x[i];
                        }
                    }
                }
                if (x_en[i] == 4){
                    if (x_index[i] > (history[1464] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2944] += 1;
                        }
                        if (isnan(history[2945])){
                            history[2945] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 10){
                    if (x_index[i] > (history[1460] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2946] += 1;
                        }
                        if (isnan(history[2947])){
                            history[2947] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1436] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2948] += 1;
                        }
                        if (isnan(history[2949])){
                            history[2949] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1480] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2950] += 1;
                        }
                        if (isnan(history[2951])){
                            history[2951] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 5){
                    if (x_index[i] > (history[1466] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2952] += 1;
                        }
                        history[2953] = x_et[i];
                    }
                }
                if (x_room_fqid_numerical[i] == 17){
                    if (x_index[i] > (history[1429] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2954] += 1;
                        }
                        if (isnan(history[2955])){
                            history[2955] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 16){
                    if (x_index[i] > (history[1471] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2956] += 1;
                        }
                        history[2957] = x_et[i];
                    }
                }
            } else if (level[i] == 11){
                if (x_text_fqid_numerical[i] == 86){
                    if (x_index[i] > (history[1512] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2958] += 1;
                        }
                        history[2959] = x_index[i];
                    }
                }
                else if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[1533] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2960] += 1;
                        }
                        if (isnan(history[2961])){
                            history[2961] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 23){
                    if (x_index[i] > (history[1485] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2962] += 1;
                        }
                        if (isnan(history[2963])){
                            history[2963] = x_et[i];
                        }
                    }
                }
                if (x_fqids[i] == 45){
                    if (x_index[i] > (history[1565] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2964] += 1;
                        }
                        history[2965] = x_index[i];
                    }
                }
                else if (x_fqids[i] == 48){
                    if (x_index[i] > (history[1614] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2966] += 1;
                        }
                        if (isnan(history[2967])){
                            history[2967] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 46){
                    if (x_index[i] > (history[1599] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2968] += 1;
                        }
                        if (isnan(history[2969])){
                            history[2969] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1512] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2970] += 1;
                        }
                        if (isnan(history[2971])){
                            history[2971] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 128){
                    if (x_index[i] > (history[1593] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2972] += 1;
                        }
                        if (isnan(history[2973])){
                            history[2973] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 114){
                    if (x_index[i] > (history[1494] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2974] += 1;
                        }
                        if (isnan(history[2975])){
                            history[2975] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 116){
                    if (x_index[i] > (history[1554] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2976] += 1;
                        }
                        if (isnan(history[2977])){
                            history[2977] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 47){
                    if (x_index[i] > (history[1523] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2978] += 1;
                        }
                        if (isnan(history[2979])){
                            history[2979] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 101){
                    if (x_index[i] > (history[1582] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2980] += 1;
                        }
                        if (isnan(history[2981])){
                            history[2981] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 122){
                    if (x_index[i] > (history[1614] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[2982] += 1;
                        }
                        if (isnan(history[2983])){
                            history[2983] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 44){
                    if (x_index[i] > (history[1533] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2984] += 1;
                        }
                        if (isnan(history[2985])){
                            history[2985] = x_index[i];
                        }
                    }
                }
                else if (x_fqids[i] == 120){
                    if (x_index[i] > (history[1607] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[2986] += 1;
                        }
                        history[2987] = x_index[i];
                    }
                }
                if (x_index[i] > (history[1486] + 0.5)){
                    if (x_index[i] < (history[1501] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2988] += 1;
                        }
                        if ((isnan(et_since_prev) == false) & (et_since_prev > history[2989])){
                            history[2989] = et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1576] + 0.5)){
                    if (x_index[i] < (history[1520] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[2990] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[2991] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1504] + 0.5)){
                    if (x_index[i] < (history[1556] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2992] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2993])){
                            history[2993] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1574] + 0.5)){
                    if (x_index[i] < (history[1560] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2994] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2995])){
                            history[2995] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1563] + 0.5)){
                    if (x_index[i] < (history[1508] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2996] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false) & (x_hover_duration[i] > history[2997])){
                            history[2997] = x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1556] + 0.5)){
                    if (x_index[i] < (history[1505] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[2998] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[2999] += x_hover_duration[i];
                        }
                    }
                    if (x_index[i] < (history[1568] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[3000] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3001] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3002] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1567] + 0.5)){
                    if (x_index[i] < (history[1608] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[3003] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3004] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3005] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1538] + 0.5)){
                    if (x_index[i] < (history[1513] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[3006] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3007] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3008] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1490] + 0.5)){
                    if (x_index[i] < (history[1508] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[3009] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3010] += x_hover_duration[i];
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3011] += pow(x_hover_duration[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1490] + 0.5)){
                    if (x_index[i] < (history[1513] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3012] += 1;
                        }
                        if ((isnan(x_index[i]) == false) & (x_index[i] > history[3013])){
                            history[3013] = x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1570] + 0.5)){
                    if (x_index[i] < (history[1602] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3014] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[3015] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1565] + 0.5)){
                    if (x_index[i] < (history[1557] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3016] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[3017])){
                            history[3017] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1541] + 0.5)){
                    if (x_index[i] < (history[1543] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3018] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3019] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3020] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1610] + 0.5)){
                    if (x_index[i] < (history[1486] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3021] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3022] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3023] += pow(x_rc_y[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1546] + 0.5)){
                    if (x_index[i] < (history[1495] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3024] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3025] += x_rc_y[i];
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3026] += pow(x_rc_y[i], 2);
                        }
                    }
                    if (x_index[i] < (history[1560] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3027] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3028] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1583] + 0.5)){
                    if (x_index[i] < (history[1550] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3029] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3030] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1601] + 0.5)){
                    if (x_index[i] < (history[1517] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3031] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false) & (screen_coor_x_abs_diff1 > history[3032])){
                            history[3032] = screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1539] + 0.5)){
                    if (x_index[i] < (history[1522] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3033] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3034] += screen_coor_x_abs_diff1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3035] += pow(screen_coor_x_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1486] + 0.5)){
                    if (x_index[i] < (history[1502] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3036] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3037] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1507] + 0.5)){
                    if (x_index[i] < (history[1518] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3038] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3039] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1610] + 0.5)){
                    if (x_index[i] < (history[1578] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3040] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3041] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3042] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1580] + 0.5)){
                    if (x_index[i] < (history[1505] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3043] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3044] += x_rc_x[i];
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3045] += pow(x_rc_x[i], 2);
                        }
                    }
                }
                if (x_index[i] > (history[1565] + 0.5)){
                    if (x_index[i] < (history[1559] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3046] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3047] += screen_coor_y_abs_diff1;
                        }
                    }
                    if (x_index[i] < (history[1533] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3048] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[3049])){
                            history[3049] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1523] + 0.5)){
                    if (x_index[i] < (history[1492] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3050] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3051] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1527] + 0.5)){
                    if (x_index[i] < (history[1529] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3052] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3053] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1531] + 0.5)){
                    if (x_index[i] < (history[1527] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3054] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 < history[3055])){
                            history[3055] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1548] + 0.5)){
                    if (x_index[i] < (history[1545] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3056] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3057] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3058] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_en[i] == 6){
                    if (x_index[i] > (history[1534] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3059] += 1;
                        }
                        if (isnan(history[3060])){
                            history[3060] = x_index[i];
                        }
                    }
                }
                else if (x_en[i] == 2){
                    if (x_index[i] > (history[1554] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3061] += 1;
                        }
                        if (isnan(history[3062])){
                            history[3062] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 8){
                    if (x_index[i] > (history[1523] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3063] += 1;
                        }
                        history[3064] = x_et[i];
                    }
                }
                else if (x_en[i] == 5){
                    if (x_index[i] > (history[1602] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3065] += 1;
                        }
                        if (isnan(history[3066])){
                            history[3066] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 3){
                    if (x_index[i] > (history[1507] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3067] += 1;
                        }
                        if (isnan(history[3068])){
                            history[3068] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1614] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3069] += 1;
                        }
                        if (isnan(history[3070])){
                            history[3070] = x_et[i];
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[1572] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3071] += 1;
                        }
                        history[3072] = x_index[i];
                    }
                    if (x_index[i] > (history[1589] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3073] += 1;
                        }
                        history[3074] = x_et[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 13){
                    if (x_index[i] > (history[1523] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3075] += 1;
                        }
                        history[3076] = x_index[i];
                    }
                }
                else if (x_room_fqid_numerical[i] == 12){
                    if (x_index[i] > (history[1597] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3077] += 1;
                        }
                        if (isnan(history[3078])){
                            history[3078] = x_et[i];
                        }
                    }
                }
                else if (x_room_fqid_numerical[i] == 8){
                    if (x_index[i] > (history[1582] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3079] += 1;
                        }
                        if (isnan(history[3080])){
                            history[3080] = x_et[i];
                        }
                    }
                }
                if (x_n[i] == 1){
                    if (x_index[i] > (history[1507] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3081] += 1;
                        }
                        if (isnan(history[3082])){
                            history[3082] = x_index[i];
                        }
                    }
                }
                else if (x_n[i] == 0){
                    if (x_index[i] > (history[1562] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3083] += 1;
                        }
                        if (isnan(history[3084])){
                            history[3084] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1499] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3085] += 1;
                        }
                        if (isnan(history[3086])){
                            history[3086] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 2){
                    if (x_index[i] > (history[1614] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3087] += 1;
                        }
                        if (isnan(history[3088])){
                            history[3088] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1601] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3089] += 1;
                        }
                        if (isnan(history[3090])){
                            history[3090] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 12){
                if (x_n[i] == 2){
                    if (x_index[i] > (history[1671] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3091] += 1;
                        }
                        if (isnan(history[3092])){
                            history[3092] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1620] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3093] += 1;
                        }
                        if (isnan(history[3094])){
                            history[3094] = x_et[i];
                        }
                    }
                }
                else if (x_n[i] == 1){
                    if (x_index[i] > (history[1671] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3095] += 1;
                        }
                        if (isnan(history[3096])){
                            history[3096] = x_et[i];
                        }
                    }
                    if (x_index[i] > (history[1627] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3097] += 1;
                        }
                        if (isnan(history[3098])){
                            history[3098] = x_index[i];
                        }
                    }
                    if (x_index[i] > (history[1673] + 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3099] += 1;
                        }
                        if (isnan(history[3100])){
                            history[3100] = x_index[i];
                        }
                    }
                }
                if (x_fqids[i] == 114){
                    if (x_index[i] > (history[1654] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3101] += 1;
                        }
                        if (isnan(history[3102])){
                            history[3102] = x_et[i];
                        }
                    }
                }
                else if (x_fqids[i] == 0){
                    if (x_index[i] > (history[1620] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3103] += 1;
                        }
                        if (isnan(history[3104])){
                            history[3104] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[1618] + 0.5)){
                    if (x_index[i] < (history[1633] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3105] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[3106])){
                            history[3106] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1662] + 0.5)){
                    if (x_index[i] < (history[1664] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3107] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3108] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1621] + 0.5)){
                    if (x_index[i] < (history[1678] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3109] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3110] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1646] + 0.5)){
                    if (x_index[i] < (history[1637] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3111] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3112] += x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1635] + 0.5)){
                    if (x_index[i] < (history[1657] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3113] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] > history[3114])){
                            history[3114] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1661] + 0.5)){
                    if (x_index[i] < (history[1641] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3115] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3116] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1656] + 0.5)){
                    if (x_index[i] < (history[1678] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3117] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false) & (x_rc_y[i] < history[3118])){
                            history[3118] = x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1644] + 0.5)){
                    if (x_index[i] < (history[1638] - 0.5)){
                        if (isnan(x_rc_y[i]) == false){
                            history[3119] += 1;
                        }
                        if ((isnan(x_rc_y[i]) == false)){
                            history[3120] += x_rc_y[i];
                        }
                    }
                }
                if (x_index[i] > (history[1673] + 0.5)){
                    if (x_index[i] < (history[1659] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3121] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[3122])){
                            history[3122] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1685] + 0.5)){
                    if (x_index[i] < (history[1638] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3123] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[3124])){
                            history[3124] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1643] + 0.5)){
                    if (x_index[i] < (history[1680] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3125] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3126] += screen_coor_y_abs_diff1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3127] += pow(screen_coor_y_abs_diff1, 2);
                        }
                    }
                }
                if (x_index[i] > (history[1674] + 0.5)){
                    if (x_index[i] < (history[1640] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[3128] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[3129] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1682] + 0.5)){
                    if (x_index[i] < (history[1666] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[3130] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[3131] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1676] + 0.5)){
                    if (x_index[i] < (history[1621] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3132] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[3133] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1687] + 0.5)){
                    if (x_index[i] < (history[1667] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3134] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[3135] += x_index[i];
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[3136] += pow(x_index[i], 2);
                        }
                    }
                }
                if (x_room_fqid_numerical[i] == 11){
                    if (x_index[i] > (history[1650] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3137] += 1;
                        }
                        if (isnan(history[3138])){
                            history[3138] = x_et[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 0){
                    if (x_index[i] > (history[1631] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3139] += 1;
                        }
                        if (isnan(history[3140])){
                            history[3140] = x_et[i];
                        }
                    }
                }
                else if (x_text_fqid_numerical[i] == 47){
                    if (x_index[i] > (history[1627] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3141] += 1;
                        }
                        if (isnan(history[3142])){
                            history[3142] = x_et[i];
                        }
                    }
                }
            }
        }
    } else if (lg == 2){

        for (int i=0; i < n; i++){
        
            
            if ((i != 0) & (level[i] == level[i-1])){
                screen_coor_y_abs_diff1 = abs(x_sc_y[i-1] - x_sc_y[i]);
                screen_coor_x_abs_diff1 = abs(x_sc_x[i-1] - x_sc_x[i]);
            } else {
                screen_coor_y_abs_diff1 = NAN;
                screen_coor_x_abs_diff1 = NAN;
            }
                
            
            if ((i != 0) & (level[i] == level[i-1])){
                et_since_prev = x_et[i] - x_et[i-1];
            } else {
                et_since_prev = NAN;
            }

            if (isnan(et_since_prev)){
                et_since_prev = 0;
            }
            if (et_since_prev < 0){
                et_since_prev = 0;
            }
            if (et_since_prev > 1e9){
                et_since_prev = 1e9;
            }
                
            if (level[i] == 13){
                if (x_index[i] > (history[1717] + 0.5)){
                    if (x_index[i] < (history[1719] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3143] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3144] += x_rc_x[i];
                        }
                    }
                }
            } else if (level[i] == 15){
                if (x_index[i] > (history[1723] + 0.5)){
                    if (x_index[i] < (history[1729] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3145] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false)){
                            history[3146] += x_rc_x[i];
                        }
                    }
                }
                if (x_en[i] == 3){
                    if (x_index[i] > (history[1727] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3147] += 1;
                        }
                        if (isnan(history[3148])){
                            history[3148] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 18){
                if (x_index[i] > (history[1731] + 0.5)){
                    if (x_index[i] < (history[1735] - 0.5)){
                        if (isnan(et_since_prev) == false){
                            history[3149] += 1;
                        }
                        if ((isnan(et_since_prev) == false)){
                            history[3150] += et_since_prev;
                        }
                    }
                }
                if (x_index[i] > (history[1737] + 0.5)){
                    if (x_index[i] < (history[1733] - 0.5)){
                        if (isnan(x_index[i]) == false){
                            history[3151] += 1;
                        }
                        if ((isnan(x_index[i]) == false)){
                            history[3152] += x_index[i];
                        }
                    }
                }
                if (x_index[i] > (history[1739] + 0.5)){
                    if (x_index[i] < (history[1741] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3153] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3154] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_n[i] == 2){
                    if (x_index[i] > (history[1745] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3155] += 1;
                        }
                        if (isnan(history[3156])){
                            history[3156] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 19){
                if (x_index[i] > (history[1747] + 0.5)){
                    if (x_index[i] < (history[1749] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3157] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] > history[3158])){
                            history[3158] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1751] + 0.5)){
                    if (x_index[i] < (history[1749] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3159] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false)){
                            history[3160] += screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 118){
                    if (x_index[i] > (history[1755] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3161] += 1;
                        }
                        if (isnan(history[3162])){
                            history[3162] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 20){
                if (x_fqids[i] == 86){
                    if (x_index[i] > (history[1767] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3163] += 1;
                        }
                        if (isnan(history[3164])){
                            history[3164] = x_et[i];
                        }
                    }
                }
                if (x_index[i] > (history[1757] + 0.5)){
                    if (x_index[i] < (history[1759] - 0.5)){
                        if (isnan(screen_coor_y_abs_diff1) == false){
                            history[3165] += 1;
                        }
                        if ((isnan(screen_coor_y_abs_diff1) == false) & (screen_coor_y_abs_diff1 > history[3166])){
                            history[3166] = screen_coor_y_abs_diff1;
                        }
                    }
                }
                if (x_en[i] == 6){
                    if (x_index[i] > (history[1767] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3167] += 1;
                        }
                        if (isnan(history[3168])){
                            history[3168] = x_et[i];
                        }
                    }
                }
                else if (x_en[i] == 8){
                    if (x_index[i] > (history[1763] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3169] += 1;
                        }
                        if (isnan(history[3170])){
                            history[3170] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 21){
                if (x_index[i] > (history[1769] + 0.5)){
                    if (x_index[i] < (history[1771] - 0.5)){
                        if (isnan(x_hover_duration[i]) == false){
                            history[3171] += 1;
                        }
                        if ((isnan(x_hover_duration[i]) == false)){
                            history[3172] += x_hover_duration[i];
                        }
                    }
                }
                if (x_index[i] > (history[1775] + 0.5)){
                    if (x_index[i] < (history[1779] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3173] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3174] += screen_coor_x_abs_diff1;
                        }
                    }
                }
                if (x_index[i] > (history[1775] + 0.5)){
                    if (x_index[i] < (history[1781] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3175] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[3176])){
                            history[3176] = x_rc_x[i];
                        }
                    }
                }
                if (x_index[i] > (history[1777] + 0.5)){
                    if (x_index[i] < (history[1773] - 0.5)){
                        if (isnan(x_rc_x[i]) == false){
                            history[3177] += 1;
                        }
                        if ((isnan(x_rc_x[i]) == false) & (x_rc_x[i] < history[3178])){
                            history[3178] = x_rc_x[i];
                        }
                    }
                }
                if (x_text_fqid_numerical[i] == 81){
                    if (x_index[i] > (history[1785] + 0.5)){
                        if (isnan(x_et[i]) == false){
                            history[3179] += 1;
                        }
                        if (isnan(history[3180])){
                            history[3180] = x_et[i];
                        }
                    }
                }
            } else if (level[i] == 22){
                if (x_index[i] > (history[1787] + 0.5)){
                    if (x_index[i] < (history[1789] - 0.5)){
                        if (isnan(screen_coor_x_abs_diff1) == false){
                            history[3181] += 1;
                        }
                        if ((isnan(screen_coor_x_abs_diff1) == false)){
                            history[3182] += screen_coor_x_abs_diff1;
                        }
                    }
                }
            }
        }
    }
}


    
void add_features(int lg, float* out, double* history){

    float temp;
    double temp_mean;

    if (lg >= 0){
        if (history[117] == 0){
            out[667] = NAN;
        } else {
            temp = ((history[118] == -INFINITY) ? NAN : history[118]);
            out[667] = temp;
        }
        if (history[119] == 0){
            out[668] = NAN;
        } else {
            out[668] = history[120];
        }
        if (history[119] == 0){
            out[669] = NAN;
        } else {
            out[669] = history[120]/history[119];
        }
        if (history[121] == 0){
            out[670] = NAN;
        } else {
            out[670] = history[122];
        }
        if (history[121] == 0){
            out[671] = NAN;
        } else {
            out[671] = history[122]/history[121];
        }
        if (history[123] == 0){
            out[672] = NAN;
        } else {
            out[672] = history[124];
        }
        if (history[123] == 0){
            out[673] = NAN;
        } else {
            out[673] = history[124]/history[123];
        }
        if (history[125] == 0){
            out[674] = NAN;
        } else {
            temp_mean = history[126]/history[125];
            out[674] = sqrt((
                history[127] - pow(temp_mean, 2) * history[125]
            )/(history[125]-1));
        }
        if (history[128] == 0){
            out[675] = NAN;
        } else {
            temp_mean = history[129]/history[128];
            out[675] = sqrt((
                history[130] - pow(temp_mean, 2) * history[128]
            )/(history[128]-1));
        }
        if (history[131] == 0){
            out[676] = NAN;
        } else {
            temp_mean = history[132]/history[131];
            out[676] = sqrt((
                history[133] - pow(temp_mean, 2) * history[131]
            )/(history[131]-1));
        }
        if (history[134] == 0){
            out[677] = NAN;
        } else {
            temp = ((history[135] == -INFINITY) ? NAN : history[135]);
            out[677] = temp;
        }
        if (history[134] == 0){
            out[678] = NAN;
        } else {
            out[678] = history[136];
        }
        if (history[134] == 0){
            out[679] = NAN;
        } else {
            temp_mean = history[136]/history[134];
            out[679] = sqrt((
                history[137] - pow(temp_mean, 2) * history[134]
            )/(history[134]-1));
        }
        if (history[138] == 0){
            out[680] = NAN;
        } else {
            out[680] = history[139];
        }
        out[681] = history[140];
        if (history[141] == 0){
            out[682] = NAN;
        } else {
            out[682] = history[142];
        }
        if (history[141] == 0){
            out[683] = NAN;
        } else {
            temp_mean = history[142]/history[141];
            out[683] = sqrt((
                history[143] - pow(temp_mean, 2) * history[141]
            )/(history[141]-1));
        }
        out[684] = history[144];
        if (history[145] == 0){
            out[685] = NAN;
        } else {
            temp = ((history[146] == -INFINITY) ? NAN : history[146]);
            out[685] = temp;
        }
        if (history[145] == 0){
            out[686] = NAN;
        } else {
            out[686] = history[147];
        }
        if (history[145] == 0){
            out[687] = NAN;
        } else {
            out[687] = history[147]/history[145];
        }
        if (history[148] == 0){
            out[688] = NAN;
        } else {
            temp = ((history[149] == -INFINITY) ? NAN : history[149]);
            out[688] = temp;
        }
        if (history[148] == 0){
            out[689] = NAN;
        } else {
            temp_mean = history[150]/history[148];
            out[689] = sqrt((
                history[151] - pow(temp_mean, 2) * history[148]
            )/(history[148]-1));
        }
        if (history[152] == 0){
            out[690] = NAN;
        } else {
            out[690] = history[153];
        }
        if (history[154] == 0){
            out[691] = NAN;
        } else {
            out[691] = ((history[155] == INFINITY) ? NAN : history[155]);
        }
        if (history[156] == 0){
            out[692] = NAN;
        } else {
            out[692] = ((history[157] == INFINITY) ? NAN : history[157]);
        }
        if (history[156] == 0){
            out[693] = NAN;
        } else {
            temp = ((history[158] == -INFINITY) ? NAN : history[158]);
            out[693] = temp;
        }
        if (history[156] == 0){
            out[694] = NAN;
        } else {
            out[694] = history[159]/history[156];
        }
        if (history[160] == 0){
            out[695] = NAN;
        } else {
            out[695] = ((history[161] == INFINITY) ? NAN : history[161]);
        }
        if (history[160] == 0){
            out[696] = NAN;
        } else {
            temp = ((history[162] == -INFINITY) ? NAN : history[162]);
            out[696] = temp;
        }
        if (history[160] == 0){
            out[697] = NAN;
        } else {
            out[697] = history[163];
        }
        if (history[160] == 0){
            out[698] = NAN;
        } else {
            out[698] = history[163]/history[160];
        }
        if (history[160] == 0){
            out[699] = NAN;
        } else {
            temp_mean = history[163]/history[160];
            out[699] = sqrt((
                history[164] - pow(temp_mean, 2) * history[160]
            )/(history[160]-1));
        }
        if (history[165] == 0){
            out[700] = NAN;
        } else {
            out[700] = ((history[166] == INFINITY) ? NAN : history[166]);
        }
        if (history[165] == 0){
            out[701] = NAN;
        } else {
            out[701] = history[167];
        }
        if (history[168] == 0){
            out[702] = NAN;
        } else {
            temp_mean = history[169]/history[168];
            out[702] = sqrt((
                history[170] - pow(temp_mean, 2) * history[168]
            )/(history[168]-1));
        }
        if (history[171] == 0){
            out[703] = NAN;
        } else {
            temp = ((history[172] == -INFINITY) ? NAN : history[172]);
            out[703] = temp;
        }
        if (history[171] == 0){
            out[704] = NAN;
        } else {
            out[704] = history[173];
        }
        out[705] = history[174];
        if (history[175] == 0){
            out[706] = NAN;
        } else {
            out[706] = ((history[176] == INFINITY) ? NAN : history[176]);
        }
        if (history[177] == 0){
            out[707] = NAN;
        } else {
            temp = ((history[178] == -INFINITY) ? NAN : history[178]);
            out[707] = temp;
        }
        out[708] = history[179];
        if (history[180] == 0){
            out[709] = NAN;
        } else {
            out[709] = ((history[181] == INFINITY) ? NAN : history[181]);
        }
        if (history[182] == 0){
            out[710] = NAN;
        } else {
            out[710] = ((history[183] == INFINITY) ? NAN : history[183]);
        }
        if (history[182] == 0){
            out[711] = NAN;
        } else {
            out[711] = history[184];
        }
        if (history[185] == 0){
            out[712] = NAN;
        } else {
            out[712] = ((history[186] == INFINITY) ? NAN : history[186]);
        }
        if (history[185] == 0){
            out[713] = NAN;
        } else {
            temp_mean = history[187]/history[185];
            out[713] = sqrt((
                history[188] - pow(temp_mean, 2) * history[185]
            )/(history[185]-1));
        }
        out[714] = history[189];
        if (history[190] == 0){
            out[715] = NAN;
        } else {
            out[715] = ((history[191] == INFINITY) ? NAN : history[191]);
        }
        if (history[192] == 0){
            out[716] = NAN;
        } else {
            out[716] = ((history[193] == INFINITY) ? NAN : history[193]);
        }
        if (history[192] == 0){
            out[717] = NAN;
        } else {
            out[717] = history[194];
        }
        if (history[195] == 0){
            out[718] = NAN;
        } else {
            out[718] = ((history[196] == INFINITY) ? NAN : history[196]);
        }
        if (history[197] == 0){
            out[719] = NAN;
        } else {
            temp = ((history[198] == -INFINITY) ? NAN : history[198]);
            out[719] = temp;
        }
        if (history[197] == 0){
            out[720] = NAN;
        } else {
            out[720] = history[199]/history[197];
        }
        out[721] = history[200];
        if (history[201] == 0){
            out[722] = NAN;
        } else {
            temp_mean = history[202]/history[201];
            out[722] = sqrt((
                history[203] - pow(temp_mean, 2) * history[201]
            )/(history[201]-1));
        }
        if (history[204] == 0){
            out[723] = NAN;
        } else {
            out[723] = ((history[205] == INFINITY) ? NAN : history[205]);
        }
        if (history[204] == 0){
            out[724] = NAN;
        } else {
            temp = ((history[206] == -INFINITY) ? NAN : history[206]);
            out[724] = temp;
        }
        if (history[204] == 0){
            out[725] = NAN;
        } else {
            out[725] = history[207];
        }
        if (history[204] == 0){
            out[726] = NAN;
        } else {
            out[726] = history[207]/history[204];
        }
        if (history[208] == 0){
            out[727] = NAN;
        } else {
            out[727] = ((history[209] == INFINITY) ? NAN : history[209]);
        }
        if (history[210] == 0){
            out[728] = NAN;
        } else {
            out[728] = ((history[211] == INFINITY) ? NAN : history[211]);
        }
        if (history[210] == 0){
            out[729] = NAN;
        } else {
            temp = ((history[212] == -INFINITY) ? NAN : history[212]);
            out[729] = temp;
        }
        if (history[210] == 0){
            out[730] = NAN;
        } else {
            out[730] = history[213];
        }
        if (history[210] == 0){
            out[731] = NAN;
        } else {
            out[731] = history[213]/history[210];
        }
        if (history[210] == 0){
            out[732] = NAN;
        } else {
            temp_mean = history[213]/history[210];
            out[732] = sqrt((
                history[214] - pow(temp_mean, 2) * history[210]
            )/(history[210]-1));
        }
        if (history[215] == 0){
            out[733] = NAN;
        } else {
            out[733] = history[216]/history[215];
        }
        if (history[215] == 0){
            out[734] = NAN;
        } else {
            temp_mean = history[216]/history[215];
            out[734] = sqrt((
                history[217] - pow(temp_mean, 2) * history[215]
            )/(history[215]-1));
        }
        if (history[218] == 0){
            out[735] = NAN;
        } else {
            temp_mean = history[219]/history[218];
            out[735] = sqrt((
                history[220] - pow(temp_mean, 2) * history[218]
            )/(history[218]-1));
        }
        if (history[221] == 0){
            out[736] = NAN;
        } else {
            temp = ((history[222] == -INFINITY) ? NAN : history[222]);
            out[736] = temp;
        }
        out[737] = history[223];
        if (history[224] == 0){
            out[738] = NAN;
        } else {
            out[738] = history[225];
        }
        if (history[226] == 0){
            out[739] = NAN;
        } else {
            temp = ((history[227] == -INFINITY) ? NAN : history[227]);
            out[739] = temp;
        }
        if (history[226] == 0){
            out[740] = NAN;
        } else {
            out[740] = history[228]/history[226];
        }
        if (history[229] == 0){
            out[741] = NAN;
        } else {
            temp_mean = history[230]/history[229];
            out[741] = sqrt((
                history[231] - pow(temp_mean, 2) * history[229]
            )/(history[229]-1));
        }
        if (history[232] == 0){
            out[742] = NAN;
        } else {
            out[742] = history[233];
        }
        if (history[234] == 0){
            out[743] = NAN;
        } else {
            temp = ((history[235] == -INFINITY) ? NAN : history[235]);
            out[743] = temp;
        }
        if (history[236] == 0){
            out[744] = NAN;
        } else {
            out[744] = ((history[237] == INFINITY) ? NAN : history[237]);
        }
        if (history[238] == 0){
            out[745] = NAN;
        } else {
            temp = ((history[239] == -INFINITY) ? NAN : history[239]);
            out[745] = temp;
        }
        if (history[238] == 0){
            out[746] = NAN;
        } else {
            out[746] = history[240];
        }
        if (history[238] == 0){
            out[747] = NAN;
        } else {
            out[747] = history[240]/history[238];
        }
        if (history[241] == 0){
            out[748] = NAN;
        } else {
            out[748] = ((history[242] == INFINITY) ? NAN : history[242]);
        }
        if (history[241] == 0){
            out[749] = NAN;
        } else {
            out[749] = history[243];
        }
        if (history[241] == 0){
            out[750] = NAN;
        } else {
            out[750] = history[243]/history[241];
        }
        if (history[241] == 0){
            out[751] = NAN;
        } else {
            temp_mean = history[243]/history[241];
            out[751] = sqrt((
                history[244] - pow(temp_mean, 2) * history[241]
            )/(history[241]-1));
        }
        if (history[245] == 0){
            out[752] = NAN;
        } else {
            out[752] = ((history[246] == INFINITY) ? NAN : history[246]);
        }
        if (history[245] == 0){
            out[753] = NAN;
        } else {
            temp = ((history[247] == -INFINITY) ? NAN : history[247]);
            out[753] = temp;
        }
        if (history[248] == 0){
            out[754] = NAN;
        } else {
            temp = ((history[249] == -INFINITY) ? NAN : history[249]);
            out[754] = temp;
        }
        if (history[248] == 0){
            out[755] = NAN;
        } else {
            out[755] = history[250];
        }
        if (history[248] == 0){
            out[756] = NAN;
        } else {
            out[756] = history[250]/history[248];
        }
        if (history[251] == 0){
            out[757] = NAN;
        } else {
            temp_mean = history[252]/history[251];
            out[757] = sqrt((
                history[253] - pow(temp_mean, 2) * history[251]
            )/(history[251]-1));
        }
        if (history[254] == 0){
            out[758] = NAN;
        } else {
            out[758] = ((history[255] == INFINITY) ? NAN : history[255]);
        }
        if (history[254] == 0){
            out[759] = NAN;
        } else {
            temp = ((history[256] == -INFINITY) ? NAN : history[256]);
            out[759] = temp;
        }
        if (history[254] == 0){
            out[760] = NAN;
        } else {
            out[760] = history[257];
        }
        if (history[258] == 0){
            out[761] = NAN;
        } else {
            out[761] = history[259];
        }
        if (history[260] == 0){
            out[762] = NAN;
        } else {
            temp = ((history[261] == -INFINITY) ? NAN : history[261]);
            out[762] = temp;
        }
        if (history[260] == 0){
            out[763] = NAN;
        } else {
            out[763] = history[262];
        }
        if (history[260] == 0){
            out[764] = NAN;
        } else {
            out[764] = history[262]/history[260];
        }
        if (history[260] == 0){
            out[765] = NAN;
        } else {
            temp_mean = history[262]/history[260];
            out[765] = sqrt((
                history[263] - pow(temp_mean, 2) * history[260]
            )/(history[260]-1));
        }
        if (history[264] == 0){
            out[766] = NAN;
        } else {
            out[766] = ((history[265] == INFINITY) ? NAN : history[265]);
        }
        if (history[264] == 0){
            out[767] = NAN;
        } else {
            out[767] = history[266];
        }
        if (history[264] == 0){
            out[768] = NAN;
        } else {
            out[768] = history[266]/history[264];
        }
        if (history[264] == 0){
            out[769] = NAN;
        } else {
            temp_mean = history[266]/history[264];
            out[769] = sqrt((
                history[267] - pow(temp_mean, 2) * history[264]
            )/(history[264]-1));
        }
        if (history[1796] == 0){
            out[770] = NAN;
        } else {
            temp = ((history[1797] == -INFINITY) ? NAN : history[1797]);
            out[770] = temp;
        }
        if (history[1798] == 0){
            out[771] = NAN;
        } else {
            out[771] = history[1799]/history[1798];
        }
        if (history[1800] == 0){
            out[772] = NAN;
        } else {
            out[772] = history[1801]/history[1800];
        }
        if (history[1802] == 0){
            out[773] = NAN;
        } else {
            out[773] = history[1803]/history[1802];
        }
        if (history[1804] == 0){
            out[774] = NAN;
        } else {
            out[774] = ((history[1805] == INFINITY) ? NAN : history[1805]);
        }
        if (history[1806] == 0){
            out[775] = NAN;
        } else {
            temp = ((history[1807] == -INFINITY) ? NAN : history[1807]);
            out[775] = temp;
        }
        if (history[1808] == 0){
            out[776] = NAN;
        } else {
            temp = ((history[1809] == -INFINITY) ? NAN : history[1809]);
            out[776] = temp;
        }
        if (history[1810] == 0){
            out[777] = NAN;
        } else {
            out[777] = history[1811]/history[1810];
        }
        if (history[1812] == 0){
            out[778] = NAN;
        } else {
            temp = ((history[1813] == -INFINITY) ? NAN : history[1813]);
            out[778] = temp;
        }
        if (history[1814] == 0){
            out[779] = NAN;
        } else {
            out[779] = history[1815]/history[1814];
        }
        if (history[1816] == 0){
            out[780] = NAN;
        } else {
            temp_mean = history[1817]/history[1816];
            out[780] = sqrt((
                history[1818] - pow(temp_mean, 2) * history[1816]
            )/(history[1816]-1));
        }
            out[781] = history[1791] - history[280];
        if (history[1819] == 0){
            out[782] = NAN;
        } else {
            temp = ((history[1820] == -INFINITY) ? NAN : history[1820]);
            out[782] = temp;
        }
        if (history[1821] == 0){
            out[783] = NAN;
        } else {
            out[783] = ((history[1822] == INFINITY) ? NAN : history[1822]);
        }
        if (history[1823] == 0){
            out[784] = NAN;
        } else {
            out[784] = ((history[1824] == INFINITY) ? NAN : history[1824]);
        }
        if (history[1825] == 0){
            out[785] = NAN;
        } else {
            out[785] = ((history[1826] == INFINITY) ? NAN : history[1826]);
        }
        if (history[1827] == 0){
            out[786] = NAN;
        } else {
            out[786] = ((history[1828] == INFINITY) ? NAN : history[1828]);
        }
        if (history[1829] == 0){
            out[787] = NAN;
        } else {
            temp = ((history[1830] == -INFINITY) ? NAN : history[1830]);
            out[787] = temp;
        }
        if (history[1831] == 0){
            out[788] = NAN;
        } else {
            temp = ((history[1832] == -INFINITY) ? NAN : history[1832]);
            out[788] = temp;
        }
        if (history[1831] == 0){
            out[789] = NAN;
        } else {
            out[789] = history[1833]/history[1831];
        }
        if (history[1834] == 0){
            out[790] = NAN;
        } else {
            out[790] = history[1835];
        }
        if (history[1836] == 0){
            out[791] = NAN;
        } else {
            temp = ((history[1837] == -INFINITY) ? NAN : history[1837]);
            out[791] = temp;
        }
        if (history[1838] == 0){
            out[792] = NAN;
        } else {
            temp = ((history[1839] == -INFINITY) ? NAN : history[1839]);
            out[792] = temp;
        }
        if (history[1840] == 0){
            out[793] = NAN;
        } else {
            out[793] = history[1841]/history[1840];
        }
        if (history[1842] == 0){
            out[794] = NAN;
        } else {
            out[794] = history[1843]/history[1842];
        }
        if (history[1844] == 0){
            out[795] = NAN;
        } else {
            out[795] = history[1845]/history[1844];
        }
        if (history[1846] == 0){
            out[796] = NAN;
        } else {
            out[796] = ((history[1847] == INFINITY) ? NAN : history[1847]);
        }
        if (history[1848] == 0){
            out[797] = NAN;
        } else {
            temp_mean = history[1849]/history[1848];
            out[797] = sqrt((
                history[1850] - pow(temp_mean, 2) * history[1848]
            )/(history[1848]-1));
        }
        if (history[1851] == 0){
            out[798] = NAN;
        } else {
            temp_mean = history[1852]/history[1851];
            out[798] = sqrt((
                history[1853] - pow(temp_mean, 2) * history[1851]
            )/(history[1851]-1));
        }
        if (history[1854] == 0){
            out[799] = NAN;
        } else {
            out[799] = history[1855];
        }
        if (history[1856] == 0){
            out[800] = NAN;
        } else {
            temp_mean = history[1857]/history[1856];
            out[800] = sqrt((
                history[1858] - pow(temp_mean, 2) * history[1856]
            )/(history[1856]-1));
        }
        if (history[1859] == 0){
            out[801] = NAN;
        } else {
            out[801] = history[1860];
        }
        if (history[1861] == 0){
            out[802] = NAN;
        } else {
            out[802] = history[1862];
        }
        if (history[1863] == 0){
            out[803] = NAN;
        } else {
            out[803] = history[1864];
        }
        if (history[1865] == 0){
            out[804] = NAN;
        } else {
            out[804] = history[1866];
        }
        if (history[1867] == 0){
            out[805] = NAN;
        } else {
            out[805] = history[1868];
        }
        if (history[1869] == 0){
            out[806] = NAN;
        } else {
            temp = ((history[1870] == -INFINITY) ? NAN : history[1870]);
            out[806] = temp;
        }
        if (history[1871] == 0){
            out[807] = NAN;
        } else {
            out[807] = history[1872];
        }
        if (history[1873] == 0){
            out[808] = NAN;
        } else {
            out[808] = ((history[1874] == INFINITY) ? NAN : history[1874]);
        }
        if (history[1875] == 0){
            out[809] = NAN;
        } else {
            out[809] = ((history[1876] == INFINITY) ? NAN : history[1876]);
        }
        if (history[1877] == 0){
            out[810] = NAN;
        } else {
            out[810] = ((history[1878] == INFINITY) ? NAN : history[1878]);
        }
        if (history[1879] == 0){
            out[811] = NAN;
        } else {
            temp_mean = history[1880]/history[1879];
            out[811] = sqrt((
                history[1881] - pow(temp_mean, 2) * history[1879]
            )/(history[1879]-1));
        }
        if (history[1882] == 0){
            out[812] = NAN;
        } else {
            temp = ((history[1883] == -INFINITY) ? NAN : history[1883]);
            out[812] = temp;
        }
        if (history[1884] == 0){
            out[813] = NAN;
        } else {
            temp = ((history[1885] == -INFINITY) ? NAN : history[1885]);
            out[813] = temp;
        }
        if (history[1886] == 0){
            out[814] = NAN;
        } else {
            out[814] = history[1887]/history[1886];
        }
        if (history[1888] == 0){
            out[815] = NAN;
        } else {
            out[815] = history[1889]/history[1888];
        }
        if (history[1890] == 0){
            out[816] = NAN;
        } else {
            out[816] = history[1891]/history[1890];
        }
        if (history[1892] == 0){
            out[817] = NAN;
        } else {
            temp_mean = history[1893]/history[1892];
            out[817] = sqrt((
                history[1894] - pow(temp_mean, 2) * history[1892]
            )/(history[1892]-1));
        }
        if (history[1895] == 0){
            out[818] = NAN;
        } else {
            temp_mean = history[1896]/history[1895];
            out[818] = sqrt((
                history[1897] - pow(temp_mean, 2) * history[1895]
            )/(history[1895]-1));
        }
        if (history[1898] == 0){
            out[819] = NAN;
        } else {
            temp_mean = history[1899]/history[1898];
            out[819] = sqrt((
                history[1900] - pow(temp_mean, 2) * history[1898]
            )/(history[1898]-1));
        }
        if (history[1901] == 0){
            out[820] = NAN;
        } else {
            out[820] = history[1902];
        }
        if (history[1903] == 0){
            out[821] = NAN;
        } else {
            out[821] = history[1904];
        }
        if (history[1905] == 0){
            out[822] = NAN;
        } else {
            out[822] = history[1906];
        }
        if (history[1907] == 0){
            out[823] = NAN;
        } else {
            out[823] = ((history[1908] == INFINITY) ? NAN : history[1908]);
        }
        if (history[1909] == 0){
            out[824] = NAN;
        } else {
            out[824] = history[1910];
        }
            out[825] = history[1914] - history[298];
            out[826] = history[1912] - history[303];
            out[827] = history[1793] - history[303];
            out[828] = history[1795] - history[278];
        if (history[1927] == 0){
            out[829] = NAN;
        } else {
            temp = ((history[1928] == -INFINITY) ? NAN : history[1928]);
            out[829] = temp;
        }
        if (history[1929] == 0){
            out[830] = NAN;
        } else {
            out[830] = ((history[1930] == INFINITY) ? NAN : history[1930]);
        }
        if (history[1931] == 0){
            out[831] = NAN;
        } else {
            out[831] = history[1932];
        }
        if (history[1933] == 0){
            out[832] = NAN;
        } else {
            temp = ((history[1934] == -INFINITY) ? NAN : history[1934]);
            out[832] = temp;
        }
        if (history[1935] == 0){
            out[833] = NAN;
        } else {
            temp = ((history[1936] == -INFINITY) ? NAN : history[1936]);
            out[833] = temp;
        }
        if (history[1937] == 0){
            out[834] = NAN;
        } else {
            temp = ((history[1938] == -INFINITY) ? NAN : history[1938]);
            out[834] = temp;
        }
        if (history[1939] == 0){
            out[835] = NAN;
        } else {
            out[835] = history[1940]/history[1939];
        }
        if (history[1941] == 0){
            out[836] = NAN;
        } else {
            out[836] = ((history[1942] == INFINITY) ? NAN : history[1942]);
        }
        if (history[1943] == 0){
            out[837] = NAN;
        } else {
            out[837] = ((history[1944] == INFINITY) ? NAN : history[1944]);
        }
        if (history[1945] == 0){
            out[838] = NAN;
        } else {
            out[838] = history[1946]/history[1945];
        }
        if (history[1947] == 0){
            out[839] = NAN;
        } else {
            out[839] = history[1948]/history[1947];
        }
        if (history[1949] == 0){
            out[840] = NAN;
        } else {
            temp_mean = history[1950]/history[1949];
            out[840] = sqrt((
                history[1951] - pow(temp_mean, 2) * history[1949]
            )/(history[1949]-1));
        }
        if (history[1952] == 0){
            out[841] = NAN;
        } else {
            out[841] = history[1953];
        }
        if (history[1954] == 0){
            out[842] = NAN;
        } else {
            out[842] = history[1955]/history[1954];
        }
        if (history[1956] == 0){
            out[843] = NAN;
        } else {
            out[843] = history[1957]/history[1956];
        }
        if (history[1958] == 0){
            out[844] = NAN;
        } else {
            out[844] = history[1959]/history[1958];
        }
        if (history[1960] == 0){
            out[845] = NAN;
        } else {
            out[845] = ((history[1961] == INFINITY) ? NAN : history[1961]);
        }
        if (history[1962] == 0){
            out[846] = NAN;
        } else {
            temp_mean = history[1963]/history[1962];
            out[846] = sqrt((
                history[1964] - pow(temp_mean, 2) * history[1962]
            )/(history[1962]-1));
        }
        if (history[1965] == 0){
            out[847] = NAN;
        } else {
            temp_mean = history[1966]/history[1965];
            out[847] = sqrt((
                history[1967] - pow(temp_mean, 2) * history[1965]
            )/(history[1965]-1));
        }
            out[848] = history[2001] - history[409];
            out[849] = history[1981] - history[409];
            out[850] = history[1977] - history[409];
            out[851] = history[1971] - history[399];
            out[852] = history[1920] - history[399];
            out[853] = history[2007] - history[399];
            out[854] = history[1969] - history[392];
            out[855] = history[2003] - history[392];
            out[856] = history[2009] - history[392];
            out[857] = history[1997] - history[392];
            out[858] = history[1985] - history[372];
            out[859] = history[1916] - history[382];
            out[860] = history[1918] - history[435];
            out[861] = history[1995] - history[427];
            out[862] = history[2011] - history[427];
            out[863] = history[2005] - history[440];
            out[864] = history[1999] - history[440];
            out[865] = history[1983] - history[440];
            out[866] = history[1979] - history[440];
            out[867] = history[1973] - history[416];
            out[868] = history[1926] - history[422];
            out[869] = history[1987] - history[422];
            out[870] = history[1922] - history[363];
            out[871] = history[2013] - history[352];
            out[872] = history[1975] - history[359];
            out[873] = history[2015] - history[359];
            out[874] = history[1989] - history[359];
            out[875] = history[1991] - history[390];
            out[876] = history[1993] - history[428];
            out[877] = history[1924] - history[424];
        out[878] = history[412];
        if (history[2028] == 0){
            out[879] = NAN;
        } else {
            temp = ((history[2029] == -INFINITY) ? NAN : history[2029]);
            out[879] = temp;
        }
        if (history[2030] == 0){
            out[880] = NAN;
        } else {
            temp = ((history[2031] == -INFINITY) ? NAN : history[2031]);
            out[880] = temp;
        }
        if (history[2032] == 0){
            out[881] = NAN;
        } else {
            out[881] = history[2033]/history[2032];
        }
        if (history[2034] == 0){
            out[882] = NAN;
        } else {
            out[882] = ((history[2035] == INFINITY) ? NAN : history[2035]);
        }
        if (history[2036] == 0){
            out[883] = NAN;
        } else {
            temp = ((history[2037] == -INFINITY) ? NAN : history[2037]);
            out[883] = temp;
        }
        if (history[2038] == 0){
            out[884] = NAN;
        } else {
            out[884] = history[2039]/history[2038];
        }
        if (history[2040] == 0){
            out[885] = NAN;
        } else {
            out[885] = history[2041];
        }
        if (history[2042] == 0){
            out[886] = NAN;
        } else {
            out[886] = ((history[2043] == INFINITY) ? NAN : history[2043]);
        }
        if (history[2044] == 0){
            out[887] = NAN;
        } else {
            out[887] = ((history[2045] == INFINITY) ? NAN : history[2045]);
        }
        if (history[2046] == 0){
            out[888] = NAN;
        } else {
            temp_mean = history[2047]/history[2046];
            out[888] = sqrt((
                history[2048] - pow(temp_mean, 2) * history[2046]
            )/(history[2046]-1));
        }
        if (history[2049] == 0){
            out[889] = NAN;
        } else {
            out[889] = ((history[2050] == INFINITY) ? NAN : history[2050]);
        }
            out[890] = history[2017] - history[464];
            out[891] = history[2082] - history[464];
            out[892] = history[2025] - history[457];
            out[893] = history[2019] - history[497];
            out[894] = history[2072] - history[468];
            out[895] = history[2027] - history[458];
            out[896] = history[2021] - history[477];
            out[897] = history[2074] - history[477];
        if (history[2051] == 0){
            out[898] = NAN;
        } else {
            out[898] = ((history[2052] == INFINITY) ? NAN : history[2052]);
        }
        if (history[2053] == 0){
            out[899] = NAN;
        } else {
            temp_mean = history[2054]/history[2053];
            out[899] = sqrt((
                history[2055] - pow(temp_mean, 2) * history[2053]
            )/(history[2053]-1));
        }
        if (history[2056] == 0){
            out[900] = NAN;
        } else {
            temp_mean = history[2057]/history[2056];
            out[900] = sqrt((
                history[2058] - pow(temp_mean, 2) * history[2056]
            )/(history[2056]-1));
        }
        if (history[2059] == 0){
            out[901] = NAN;
        } else {
            temp_mean = history[2060]/history[2059];
            out[901] = sqrt((
                history[2061] - pow(temp_mean, 2) * history[2059]
            )/(history[2059]-1));
        }
        if (history[2062] == 0){
            out[902] = NAN;
        } else {
            temp_mean = history[2063]/history[2062];
            out[902] = sqrt((
                history[2064] - pow(temp_mean, 2) * history[2062]
            )/(history[2062]-1));
        }
        if (history[2065] == 0){
            out[903] = NAN;
        } else {
            out[903] = history[2066];
        }
            out[904] = history[2076] - history[507];
            out[905] = history[2078] - history[500];
            out[906] = history[2068] - history[486];
            out[907] = history[2080] - history[490];
            out[908] = history[2070] - history[470];
            out[909] = history[2023] - history[447];
        if (history[2093] == 0){
            out[910] = NAN;
        } else {
            temp = ((history[2094] == -INFINITY) ? NAN : history[2094]);
            out[910] = temp;
        }
        if (history[2095] == 0){
            out[911] = NAN;
        } else {
            temp = ((history[2096] == -INFINITY) ? NAN : history[2096]);
            out[911] = temp;
        }
        if (history[2097] == 0){
            out[912] = NAN;
        } else {
            out[912] = ((history[2098] == INFINITY) ? NAN : history[2098]);
        }
        if (history[2099] == 0){
            out[913] = NAN;
        } else {
            out[913] = ((history[2100] == INFINITY) ? NAN : history[2100]);
        }
        if (history[2101] == 0){
            out[914] = NAN;
        } else {
            out[914] = ((history[2102] == INFINITY) ? NAN : history[2102]);
        }
        if (history[2103] == 0){
            out[915] = NAN;
        } else {
            out[915] = ((history[2104] == INFINITY) ? NAN : history[2104]);
        }
        if (history[2105] == 0){
            out[916] = NAN;
        } else {
            out[916] = ((history[2106] == INFINITY) ? NAN : history[2106]);
        }
        if (history[2107] == 0){
            out[917] = NAN;
        } else {
            out[917] = ((history[2108] == INFINITY) ? NAN : history[2108]);
        }
        if (history[2109] == 0){
            out[918] = NAN;
        } else {
            out[918] = ((history[2110] == INFINITY) ? NAN : history[2110]);
        }
        if (history[2111] == 0){
            out[919] = NAN;
        } else {
            temp_mean = history[2112]/history[2111];
            out[919] = sqrt((
                history[2113] - pow(temp_mean, 2) * history[2111]
            )/(history[2111]-1));
        }
        if (history[2114] == 0){
            out[920] = NAN;
        } else {
            temp_mean = history[2115]/history[2114];
            out[920] = sqrt((
                history[2116] - pow(temp_mean, 2) * history[2114]
            )/(history[2114]-1));
        }
        if (history[2117] == 0){
            out[921] = NAN;
        } else {
            temp_mean = history[2118]/history[2117];
            out[921] = sqrt((
                history[2119] - pow(temp_mean, 2) * history[2117]
            )/(history[2117]-1));
        }
        if (history[2120] == 0){
            out[922] = NAN;
        } else {
            temp_mean = history[2121]/history[2120];
            out[922] = sqrt((
                history[2122] - pow(temp_mean, 2) * history[2120]
            )/(history[2120]-1));
        }
        if (history[2123] == 0){
            out[923] = NAN;
        } else {
            temp = ((history[2124] == -INFINITY) ? NAN : history[2124]);
            out[923] = temp;
        }
        if (history[2125] == 0){
            out[924] = NAN;
        } else {
            out[924] = ((history[2126] == INFINITY) ? NAN : history[2126]);
        }
        if (history[2127] == 0){
            out[925] = NAN;
        } else {
            out[925] = ((history[2128] == INFINITY) ? NAN : history[2128]);
        }
        if (history[2129] == 0){
            out[926] = NAN;
        } else {
            temp_mean = history[2130]/history[2129];
            out[926] = sqrt((
                history[2131] - pow(temp_mean, 2) * history[2129]
            )/(history[2129]-1));
        }
        if (history[2132] == 0){
            out[927] = NAN;
        } else {
            out[927] = history[2133];
        }
        if (history[2134] == 0){
            out[928] = NAN;
        } else {
            out[928] = history[2135];
        }
        if (history[2136] == 0){
            out[929] = NAN;
        } else {
            out[929] = history[2137];
        }
        if (history[2138] == 0){
            out[930] = NAN;
        } else {
            temp = ((history[2139] == -INFINITY) ? NAN : history[2139]);
            out[930] = temp;
        }
        if (history[2140] == 0){
            out[931] = NAN;
        } else {
            temp = ((history[2141] == -INFINITY) ? NAN : history[2141]);
            out[931] = temp;
        }
        if (history[2142] == 0){
            out[932] = NAN;
        } else {
            out[932] = ((history[2143] == INFINITY) ? NAN : history[2143]);
        }
        if (history[2144] == 0){
            out[933] = NAN;
        } else {
            temp = ((history[2145] == -INFINITY) ? NAN : history[2145]);
            out[933] = temp;
        }
        if (history[2146] == 0){
            out[934] = NAN;
        } else {
            temp = ((history[2147] == -INFINITY) ? NAN : history[2147]);
            out[934] = temp;
        }
        if (history[2148] == 0){
            out[935] = NAN;
        } else {
            out[935] = history[2149]/history[2148];
        }
        if (history[2150] == 0){
            out[936] = NAN;
        } else {
            temp_mean = history[2151]/history[2150];
            out[936] = sqrt((
                history[2152] - pow(temp_mean, 2) * history[2150]
            )/(history[2150]-1));
        }
        if (history[2153] == 0){
            out[937] = NAN;
        } else {
            temp_mean = history[2154]/history[2153];
            out[937] = sqrt((
                history[2155] - pow(temp_mean, 2) * history[2153]
            )/(history[2153]-1));
        }
        if (history[2156] == 0){
            out[938] = NAN;
        } else {
            out[938] = history[2157];
        }
        if (history[2158] == 0){
            out[939] = NAN;
        } else {
            out[939] = history[2159]/history[2158];
        }
        if (history[2160] == 0){
            out[940] = NAN;
        } else {
            out[940] = history[2161]/history[2160];
        }
        if (history[2162] == 0){
            out[941] = NAN;
        } else {
            out[941] = history[2163]/history[2162];
        }
        if (history[2164] == 0){
            out[942] = NAN;
        } else {
            temp_mean = history[2165]/history[2164];
            out[942] = sqrt((
                history[2166] - pow(temp_mean, 2) * history[2164]
            )/(history[2164]-1));
        }
        if (history[2167] == 0){
            out[943] = NAN;
        } else {
            temp_mean = history[2168]/history[2167];
            out[943] = sqrt((
                history[2169] - pow(temp_mean, 2) * history[2167]
            )/(history[2167]-1));
        }
        if (history[2170] == 0){
            out[944] = NAN;
        } else {
            out[944] = ((history[2171] == INFINITY) ? NAN : history[2171]);
        }
            out[945] = history[2189] - history[574];
        if (history[2172] == 0){
            out[946] = NAN;
        } else {
            temp_mean = history[2173]/history[2172];
            out[946] = sqrt((
                history[2174] - pow(temp_mean, 2) * history[2172]
            )/(history[2172]-1));
        }
            out[947] = history[2090] - history[515];
            out[948] = history[2195] - history[515];
            out[949] = history[2197] - history[615];
            out[950] = history[2088] - history[547];
        if (history[2175] == 0){
            out[951] = NAN;
        } else {
            temp_mean = history[2176]/history[2175];
            out[951] = sqrt((
                history[2177] - pow(temp_mean, 2) * history[2175]
            )/(history[2175]-1));
        }
        if (history[2178] == 0){
            out[952] = NAN;
        } else {
            out[952] = history[2179];
        }
            out[953] = history[2086] - history[543];
            out[954] = history[2191] - history[526];
            out[955] = history[2181] - history[531];
            out[956] = history[2185] - history[538];
            out[957] = history[2183] - history[538];
            out[958] = history[2092] - history[554];
            out[959] = history[2187] - history[554];
            out[960] = history[2193] - history[608];
            out[961] = history[2084] - history[521];
        out[962] = history[611];
        if (history[2200] == 0){
            out[963] = NAN;
        } else {
            temp = ((history[2201] == -INFINITY) ? NAN : history[2201]);
            out[963] = temp;
        }
        if (history[2202] == 0){
            out[964] = NAN;
        } else {
            temp_mean = history[2203]/history[2202];
            out[964] = sqrt((
                history[2204] - pow(temp_mean, 2) * history[2202]
            )/(history[2202]-1));
        }
        if (history[2205] == 0){
            out[965] = NAN;
        } else {
            out[965] = history[2206];
        }
        if (history[2207] == 0){
            out[966] = NAN;
        } else {
            temp = ((history[2208] == -INFINITY) ? NAN : history[2208]);
            out[966] = temp;
        }
            out[967] = history[2199] - history[619];
        if (history[2209] == 0){
            out[968] = NAN;
        } else {
            temp = ((history[2210] == -INFINITY) ? NAN : history[2210]);
            out[968] = temp;
        }
        if (history[2211] == 0){
            out[969] = NAN;
        } else {
            temp = ((history[2212] == -INFINITY) ? NAN : history[2212]);
            out[969] = temp;
        }
        if (history[2213] == 0){
            out[970] = NAN;
        } else {
            temp = ((history[2214] == -INFINITY) ? NAN : history[2214]);
            out[970] = temp;
        }
        if (history[2215] == 0){
            out[971] = NAN;
        } else {
            out[971] = history[2216]/history[2215];
        }
        if (history[2217] == 0){
            out[972] = NAN;
        } else {
            out[972] = ((history[2218] == INFINITY) ? NAN : history[2218]);
        }
        if (history[2219] == 0){
            out[973] = NAN;
        } else {
            out[973] = ((history[2220] == INFINITY) ? NAN : history[2220]);
        }
        if (history[2221] == 0){
            out[974] = NAN;
        } else {
            out[974] = ((history[2222] == INFINITY) ? NAN : history[2222]);
        }
        if (history[2223] == 0){
            out[975] = NAN;
        } else {
            out[975] = ((history[2224] == INFINITY) ? NAN : history[2224]);
        }
        if (history[2225] == 0){
            out[976] = NAN;
        } else {
            out[976] = history[2226]/history[2225];
        }
        if (history[2227] == 0){
            out[977] = NAN;
        } else {
            out[977] = history[2228]/history[2227];
        }
        if (history[2229] == 0){
            out[978] = NAN;
        } else {
            temp_mean = history[2230]/history[2229];
            out[978] = sqrt((
                history[2231] - pow(temp_mean, 2) * history[2229]
            )/(history[2229]-1));
        }
        if (history[2232] == 0){
            out[979] = NAN;
        } else {
            temp_mean = history[2233]/history[2232];
            out[979] = sqrt((
                history[2234] - pow(temp_mean, 2) * history[2232]
            )/(history[2232]-1));
        }
        if (history[2235] == 0){
            out[980] = NAN;
        } else {
            temp_mean = history[2236]/history[2235];
            out[980] = sqrt((
                history[2237] - pow(temp_mean, 2) * history[2235]
            )/(history[2235]-1));
        }
        if (history[2238] == 0){
            out[981] = NAN;
        } else {
            out[981] = history[2239];
        }
        if (history[2240] == 0){
            out[982] = NAN;
        } else {
            out[982] = history[2241];
        }
        if (history[2242] == 0){
            out[983] = NAN;
        } else {
            out[983] = history[2243];
        }
        if (history[2244] == 0){
            out[984] = NAN;
        } else {
            out[984] = ((history[2245] == INFINITY) ? NAN : history[2245]);
        }
        if (history[2246] == 0){
            out[985] = NAN;
        } else {
            temp_mean = history[2247]/history[2246];
            out[985] = sqrt((
                history[2248] - pow(temp_mean, 2) * history[2246]
            )/(history[2246]-1));
        }
            out[986] = history[2250] - history[648];
        if (history[661] == 0){
            out[987] = NAN;
        } else {
            out[987] = history[662];
        }
        if (history[661] == 0){
            out[988] = NAN;
        } else {
            temp_mean = history[662]/history[661];
            out[988] = sqrt((
                history[663] - pow(temp_mean, 2) * history[661]
            )/(history[661]-1));
        }
        out[989] = history[641];
    }
    if (lg >= 1){
        if (history[664] == 0){
            out[990] = NAN;
        } else {
            temp = ((history[665] == -INFINITY) ? NAN : history[665]);
            out[990] = temp;
        }
        if (history[664] == 0){
            out[991] = NAN;
        } else {
            temp_mean = history[666]/history[664];
            out[991] = sqrt((
                history[667] - pow(temp_mean, 2) * history[664]
            )/(history[664]-1));
        }
        if (history[668] == 0){
            out[992] = NAN;
        } else {
            out[992] = history[669];
        }
        if (history[668] == 0){
            out[993] = NAN;
        } else {
            out[993] = history[669]/history[668];
        }
        if (history[668] == 0){
            out[994] = NAN;
        } else {
            temp_mean = history[669]/history[668];
            out[994] = sqrt((
                history[670] - pow(temp_mean, 2) * history[668]
            )/(history[668]-1));
        }
        if (history[671] == 0){
            out[995] = NAN;
        } else {
            out[995] = history[672];
        }
        if (history[671] == 0){
            out[996] = NAN;
        } else {
            out[996] = history[672]/history[671];
        }
        if (history[673] == 0){
            out[997] = NAN;
        } else {
            out[997] = history[674];
        }
        if (history[673] == 0){
            out[998] = NAN;
        } else {
            out[998] = history[674]/history[673];
        }
        if (history[675] == 0){
            out[999] = NAN;
        } else {
            temp = ((history[676] == -INFINITY) ? NAN : history[676]);
            out[999] = temp;
        }
        if (history[677] == 0){
            out[1000] = NAN;
        } else {
            temp = ((history[678] == -INFINITY) ? NAN : history[678]);
            out[1000] = temp;
        }
        if (history[677] == 0){
            out[1001] = NAN;
        } else {
            temp_mean = history[679]/history[677];
            out[1001] = sqrt((
                history[680] - pow(temp_mean, 2) * history[677]
            )/(history[677]-1));
        }
        if (history[681] == 0){
            out[1002] = NAN;
        } else {
            temp = ((history[682] == -INFINITY) ? NAN : history[682]);
            out[1002] = temp;
        }
        if (history[683] == 0){
            out[1003] = NAN;
        } else {
            out[1003] = ((history[684] == INFINITY) ? NAN : history[684]);
        }
        if (history[683] == 0){
            out[1004] = NAN;
        } else {
            temp = ((history[685] == -INFINITY) ? NAN : history[685]);
            out[1004] = temp;
        }
        if (history[683] == 0){
            out[1005] = NAN;
        } else {
            out[1005] = history[686]/history[683];
        }
        if (history[687] == 0){
            out[1006] = NAN;
        } else {
            temp = ((history[688] == -INFINITY) ? NAN : history[688]);
            out[1006] = temp;
        }
        if (history[687] == 0){
            out[1007] = NAN;
        } else {
            temp_mean = history[689]/history[687];
            out[1007] = sqrt((
                history[690] - pow(temp_mean, 2) * history[687]
            )/(history[687]-1));
        }
        if (history[691] == 0){
            out[1008] = NAN;
        } else {
            out[1008] = history[692]/history[691];
        }
        if (history[693] == 0){
            out[1009] = NAN;
        } else {
            temp = ((history[694] == -INFINITY) ? NAN : history[694]);
            out[1009] = temp;
        }
        if (history[693] == 0){
            out[1010] = NAN;
        } else {
            out[1010] = history[695];
        }
        if (history[693] == 0){
            out[1011] = NAN;
        } else {
            out[1011] = history[695]/history[693];
        }
        if (history[693] == 0){
            out[1012] = NAN;
        } else {
            temp_mean = history[695]/history[693];
            out[1012] = sqrt((
                history[696] - pow(temp_mean, 2) * history[693]
            )/(history[693]-1));
        }
        if (history[697] == 0){
            out[1013] = NAN;
        } else {
            out[1013] = ((history[698] == INFINITY) ? NAN : history[698]);
        }
        if (history[697] == 0){
            out[1014] = NAN;
        } else {
            out[1014] = history[699]/history[697];
        }
        if (history[697] == 0){
            out[1015] = NAN;
        } else {
            temp_mean = history[699]/history[697];
            out[1015] = sqrt((
                history[700] - pow(temp_mean, 2) * history[697]
            )/(history[697]-1));
        }
        if (history[701] == 0){
            out[1016] = NAN;
        } else {
            temp = ((history[702] == -INFINITY) ? NAN : history[702]);
            out[1016] = temp;
        }
        if (history[701] == 0){
            out[1017] = NAN;
        } else {
            out[1017] = history[703]/history[701];
        }
        if (history[704] == 0){
            out[1018] = NAN;
        } else {
            temp = ((history[705] == -INFINITY) ? NAN : history[705]);
            out[1018] = temp;
        }
        if (history[706] == 0){
            out[1019] = NAN;
        } else {
            out[1019] = history[707];
        }
        if (history[708] == 0){
            out[1020] = NAN;
        } else {
            out[1020] = history[709];
        }
        if (history[710] == 0){
            out[1021] = NAN;
        } else {
            out[1021] = history[711];
        }
        out[1022] = history[712];
        if (history[713] == 0){
            out[1023] = NAN;
        } else {
            out[1023] = history[714]/history[713];
        }
        if (history[715] == 0){
            out[1024] = NAN;
        } else {
            temp = ((history[716] == -INFINITY) ? NAN : history[716]);
            out[1024] = temp;
        }
        if (history[715] == 0){
            out[1025] = NAN;
        } else {
            out[1025] = history[717];
        }
        if (history[718] == 0){
            out[1026] = NAN;
        } else {
            temp = ((history[719] == -INFINITY) ? NAN : history[719]);
            out[1026] = temp;
        }
        if (history[718] == 0){
            out[1027] = NAN;
        } else {
            out[1027] = history[720];
        }
        if (history[718] == 0){
            out[1028] = NAN;
        } else {
            out[1028] = history[720]/history[718];
        }
        if (history[718] == 0){
            out[1029] = NAN;
        } else {
            temp_mean = history[720]/history[718];
            out[1029] = sqrt((
                history[721] - pow(temp_mean, 2) * history[718]
            )/(history[718]-1));
        }
        if (history[722] == 0){
            out[1030] = NAN;
        } else {
            out[1030] = ((history[723] == INFINITY) ? NAN : history[723]);
        }
        if (history[722] == 0){
            out[1031] = NAN;
        } else {
            temp = ((history[724] == -INFINITY) ? NAN : history[724]);
            out[1031] = temp;
        }
        if (history[722] == 0){
            out[1032] = NAN;
        } else {
            out[1032] = history[725];
        }
        if (history[722] == 0){
            out[1033] = NAN;
        } else {
            out[1033] = history[725]/history[722];
        }
        if (history[722] == 0){
            out[1034] = NAN;
        } else {
            temp_mean = history[725]/history[722];
            out[1034] = sqrt((
                history[726] - pow(temp_mean, 2) * history[722]
            )/(history[722]-1));
        }
        if (history[727] == 0){
            out[1035] = NAN;
        } else {
            out[1035] = ((history[728] == INFINITY) ? NAN : history[728]);
        }
        if (history[729] == 0){
            out[1036] = NAN;
        } else {
            temp = ((history[730] == -INFINITY) ? NAN : history[730]);
            out[1036] = temp;
        }
        if (history[729] == 0){
            out[1037] = NAN;
        } else {
            out[1037] = history[731];
        }
        if (history[729] == 0){
            out[1038] = NAN;
        } else {
            temp_mean = history[731]/history[729];
            out[1038] = sqrt((
                history[732] - pow(temp_mean, 2) * history[729]
            )/(history[729]-1));
        }
        if (history[733] == 0){
            out[1039] = NAN;
        } else {
            temp = ((history[734] == -INFINITY) ? NAN : history[734]);
            out[1039] = temp;
        }
        if (history[733] == 0){
            out[1040] = NAN;
        } else {
            out[1040] = history[735];
        }
        if (history[733] == 0){
            out[1041] = NAN;
        } else {
            out[1041] = history[735]/history[733];
        }
        if (history[733] == 0){
            out[1042] = NAN;
        } else {
            temp_mean = history[735]/history[733];
            out[1042] = sqrt((
                history[736] - pow(temp_mean, 2) * history[733]
            )/(history[733]-1));
        }
        if (history[737] == 0){
            out[1043] = NAN;
        } else {
            temp = ((history[738] == -INFINITY) ? NAN : history[738]);
            out[1043] = temp;
        }
        if (history[737] == 0){
            out[1044] = NAN;
        } else {
            out[1044] = history[739]/history[737];
        }
        if (history[740] == 0){
            out[1045] = NAN;
        } else {
            temp = ((history[741] == -INFINITY) ? NAN : history[741]);
            out[1045] = temp;
        }
        if (history[740] == 0){
            out[1046] = NAN;
        } else {
            out[1046] = history[742]/history[740];
        }
        if (history[743] == 0){
            out[1047] = NAN;
        } else {
            out[1047] = ((history[744] == INFINITY) ? NAN : history[744]);
        }
        if (history[743] == 0){
            out[1048] = NAN;
        } else {
            temp = ((history[745] == -INFINITY) ? NAN : history[745]);
            out[1048] = temp;
        }
        if (history[743] == 0){
            out[1049] = NAN;
        } else {
            out[1049] = history[746];
        }
        if (history[743] == 0){
            out[1050] = NAN;
        } else {
            out[1050] = history[746]/history[743];
        }
        if (history[747] == 0){
            out[1051] = NAN;
        } else {
            out[1051] = ((history[748] == INFINITY) ? NAN : history[748]);
        }
        if (history[749] == 0){
            out[1052] = NAN;
        } else {
            out[1052] = ((history[750] == INFINITY) ? NAN : history[750]);
        }
        if (history[749] == 0){
            out[1053] = NAN;
        } else {
            temp = ((history[751] == -INFINITY) ? NAN : history[751]);
            out[1053] = temp;
        }
        if (history[749] == 0){
            out[1054] = NAN;
        } else {
            out[1054] = history[752];
        }
        if (history[749] == 0){
            out[1055] = NAN;
        } else {
            out[1055] = history[752]/history[749];
        }
        if (history[749] == 0){
            out[1056] = NAN;
        } else {
            temp_mean = history[752]/history[749];
            out[1056] = sqrt((
                history[753] - pow(temp_mean, 2) * history[749]
            )/(history[749]-1));
        }
        if (history[754] == 0){
            out[1057] = NAN;
        } else {
            out[1057] = history[755]/history[754];
        }
        if (history[756] == 0){
            out[1058] = NAN;
        } else {
            out[1058] = history[757];
        }
        if (history[758] == 0){
            out[1059] = NAN;
        } else {
            out[1059] = ((history[759] == INFINITY) ? NAN : history[759]);
        }
        if (history[758] == 0){
            out[1060] = NAN;
        } else {
            temp = ((history[760] == -INFINITY) ? NAN : history[760]);
            out[1060] = temp;
        }
        if (history[758] == 0){
            out[1061] = NAN;
        } else {
            out[1061] = history[761];
        }
        if (history[758] == 0){
            out[1062] = NAN;
        } else {
            out[1062] = history[761]/history[758];
        }
        if (history[762] == 0){
            out[1063] = NAN;
        } else {
            out[1063] = ((history[763] == INFINITY) ? NAN : history[763]);
        }
        if (history[762] == 0){
            out[1064] = NAN;
        } else {
            out[1064] = history[764];
        }
        if (history[765] == 0){
            out[1065] = NAN;
        } else {
            out[1065] = ((history[766] == INFINITY) ? NAN : history[766]);
        }
        out[1066] = history[767];
        if (history[768] == 0){
            out[1067] = NAN;
        } else {
            out[1067] = ((history[769] == INFINITY) ? NAN : history[769]);
        }
        if (history[770] == 0){
            out[1068] = NAN;
        } else {
            out[1068] = history[771]/history[770];
        }
        if (history[772] == 0){
            out[1069] = NAN;
        } else {
            temp = ((history[773] == -INFINITY) ? NAN : history[773]);
            out[1069] = temp;
        }
        if (history[772] == 0){
            out[1070] = NAN;
        } else {
            out[1070] = history[774];
        }
        if (history[772] == 0){
            out[1071] = NAN;
        } else {
            out[1071] = history[774]/history[772];
        }
        if (history[775] == 0){
            out[1072] = NAN;
        } else {
            temp_mean = history[776]/history[775];
            out[1072] = sqrt((
                history[777] - pow(temp_mean, 2) * history[775]
            )/(history[775]-1));
        }
        if (history[778] == 0){
            out[1073] = NAN;
        } else {
            out[1073] = history[779]/history[778];
        }
        if (history[780] == 0){
            out[1074] = NAN;
        } else {
            out[1074] = ((history[781] == INFINITY) ? NAN : history[781]);
        }
        if (history[782] == 0){
            out[1075] = NAN;
        } else {
            temp = ((history[783] == -INFINITY) ? NAN : history[783]);
            out[1075] = temp;
        }
        if (history[782] == 0){
            out[1076] = NAN;
        } else {
            temp_mean = history[784]/history[782];
            out[1076] = sqrt((
                history[785] - pow(temp_mean, 2) * history[782]
            )/(history[782]-1));
        }
        out[1077] = history[786];
        if (history[787] == 0){
            out[1078] = NAN;
        } else {
            temp = ((history[788] == -INFINITY) ? NAN : history[788]);
            out[1078] = temp;
        }
        out[1079] = history[789];
        if (history[790] == 0){
            out[1080] = NAN;
        } else {
            temp = ((history[791] == -INFINITY) ? NAN : history[791]);
            out[1080] = temp;
        }
        if (history[790] == 0){
            out[1081] = NAN;
        } else {
            out[1081] = history[792];
        }
        if (history[790] == 0){
            out[1082] = NAN;
        } else {
            temp_mean = history[792]/history[790];
            out[1082] = sqrt((
                history[793] - pow(temp_mean, 2) * history[790]
            )/(history[790]-1));
        }
        if (history[794] == 0){
            out[1083] = NAN;
        } else {
            out[1083] = history[795];
        }
        if (history[796] == 0){
            out[1084] = NAN;
        } else {
            out[1084] = history[797]/history[796];
        }
        if (history[798] == 0){
            out[1085] = NAN;
        } else {
            temp = ((history[799] == -INFINITY) ? NAN : history[799]);
            out[1085] = temp;
        }
        if (history[798] == 0){
            out[1086] = NAN;
        } else {
            out[1086] = history[800];
        }
        if (history[801] == 0){
            out[1087] = NAN;
        } else {
            temp = ((history[802] == -INFINITY) ? NAN : history[802]);
            out[1087] = temp;
        }
        if (history[803] == 0){
            out[1088] = NAN;
        } else {
            out[1088] = ((history[804] == INFINITY) ? NAN : history[804]);
        }
        if (history[803] == 0){
            out[1089] = NAN;
        } else {
            temp_mean = history[805]/history[803];
            out[1089] = sqrt((
                history[806] - pow(temp_mean, 2) * history[803]
            )/(history[803]-1));
        }
        if (history[807] == 0){
            out[1090] = NAN;
        } else {
            out[1090] = history[808];
        }
        if (history[809] == 0){
            out[1091] = NAN;
        } else {
            out[1091] = history[810];
        }
        if (history[811] == 0){
            out[1092] = NAN;
        } else {
            out[1092] = ((history[812] == INFINITY) ? NAN : history[812]);
        }
        if (history[811] == 0){
            out[1093] = NAN;
        } else {
            temp = ((history[813] == -INFINITY) ? NAN : history[813]);
            out[1093] = temp;
        }
        if (history[811] == 0){
            out[1094] = NAN;
        } else {
            out[1094] = history[814];
        }
        if (history[811] == 0){
            out[1095] = NAN;
        } else {
            out[1095] = history[814]/history[811];
        }
        if (history[811] == 0){
            out[1096] = NAN;
        } else {
            temp_mean = history[814]/history[811];
            out[1096] = sqrt((
                history[815] - pow(temp_mean, 2) * history[811]
            )/(history[811]-1));
        }
        if (history[816] == 0){
            out[1097] = NAN;
        } else {
            out[1097] = ((history[817] == INFINITY) ? NAN : history[817]);
        }
        if (history[816] == 0){
            out[1098] = NAN;
        } else {
            temp = ((history[818] == -INFINITY) ? NAN : history[818]);
            out[1098] = temp;
        }
        if (history[816] == 0){
            out[1099] = NAN;
        } else {
            out[1099] = history[819];
        }
        if (history[816] == 0){
            out[1100] = NAN;
        } else {
            out[1100] = history[819]/history[816];
        }
        if (history[816] == 0){
            out[1101] = NAN;
        } else {
            temp_mean = history[819]/history[816];
            out[1101] = sqrt((
                history[820] - pow(temp_mean, 2) * history[816]
            )/(history[816]-1));
        }
        if (history[821] == 0){
            out[1102] = NAN;
        } else {
            out[1102] = ((history[822] == INFINITY) ? NAN : history[822]);
        }
        if (history[821] == 0){
            out[1103] = NAN;
        } else {
            temp = ((history[823] == -INFINITY) ? NAN : history[823]);
            out[1103] = temp;
        }
        if (history[821] == 0){
            out[1104] = NAN;
        } else {
            out[1104] = history[824];
        }
        if (history[821] == 0){
            out[1105] = NAN;
        } else {
            out[1105] = history[824]/history[821];
        }
        if (history[825] == 0){
            out[1106] = NAN;
        } else {
            out[1106] = ((history[826] == INFINITY) ? NAN : history[826]);
        }
        if (history[825] == 0){
            out[1107] = NAN;
        } else {
            temp = ((history[827] == -INFINITY) ? NAN : history[827]);
            out[1107] = temp;
        }
        if (history[825] == 0){
            out[1108] = NAN;
        } else {
            out[1108] = history[828];
        }
        if (history[825] == 0){
            out[1109] = NAN;
        } else {
            out[1109] = history[828]/history[825];
        }
        if (history[825] == 0){
            out[1110] = NAN;
        } else {
            temp_mean = history[828]/history[825];
            out[1110] = sqrt((
                history[829] - pow(temp_mean, 2) * history[825]
            )/(history[825]-1));
        }
        if (history[830] == 0){
            out[1111] = NAN;
        } else {
            out[1111] = ((history[831] == INFINITY) ? NAN : history[831]);
        }
        if (history[830] == 0){
            out[1112] = NAN;
        } else {
            out[1112] = history[832];
        }
        if (history[833] == 0){
            out[1113] = NAN;
        } else {
            temp = ((history[834] == -INFINITY) ? NAN : history[834]);
            out[1113] = temp;
        }
        if (history[833] == 0){
            out[1114] = NAN;
        } else {
            temp_mean = history[835]/history[833];
            out[1114] = sqrt((
                history[836] - pow(temp_mean, 2) * history[833]
            )/(history[833]-1));
        }
        if (history[837] == 0){
            out[1115] = NAN;
        } else {
            out[1115] = ((history[838] == INFINITY) ? NAN : history[838]);
        }
        if (history[839] == 0){
            out[1116] = NAN;
        } else {
            temp = ((history[840] == -INFINITY) ? NAN : history[840]);
            out[1116] = temp;
        }
        if (history[839] == 0){
            out[1117] = NAN;
        } else {
            out[1117] = history[841]/history[839];
        }
        if (history[842] == 0){
            out[1118] = NAN;
        } else {
            temp = ((history[843] == -INFINITY) ? NAN : history[843]);
            out[1118] = temp;
        }
        if (history[844] == 0){
            out[1119] = NAN;
        } else {
            out[1119] = ((history[845] == INFINITY) ? NAN : history[845]);
        }
        if (history[846] == 0){
            out[1120] = NAN;
        } else {
            temp_mean = history[847]/history[846];
            out[1120] = sqrt((
                history[848] - pow(temp_mean, 2) * history[846]
            )/(history[846]-1));
        }
        if (history[849] == 0){
            out[1121] = NAN;
        } else {
            out[1121] = ((history[850] == INFINITY) ? NAN : history[850]);
        }
        if (history[849] == 0){
            out[1122] = NAN;
        } else {
            out[1122] = history[851];
        }
        if (history[2281] == 0){
            out[1123] = NAN;
        } else {
            temp = ((history[2282] == -INFINITY) ? NAN : history[2282]);
            out[1123] = temp;
        }
        if (history[2283] == 0){
            out[1124] = NAN;
        } else {
            temp_mean = history[2284]/history[2283];
            out[1124] = sqrt((
                history[2285] - pow(temp_mean, 2) * history[2283]
            )/(history[2283]-1));
        }
        if (history[2286] == 0){
            out[1125] = NAN;
        } else {
            temp = ((history[2287] == -INFINITY) ? NAN : history[2287]);
            out[1125] = temp;
        }
        if (history[2288] == 0){
            out[1126] = NAN;
        } else {
            out[1126] = ((history[2289] == INFINITY) ? NAN : history[2289]);
        }
        if (history[2290] == 0){
            out[1127] = NAN;
        } else {
            out[1127] = history[2291]/history[2290];
        }
        if (history[2292] == 0){
            out[1128] = NAN;
        } else {
            out[1128] = ((history[2293] == INFINITY) ? NAN : history[2293]);
        }
        if (history[2294] == 0){
            out[1129] = NAN;
        } else {
            out[1129] = ((history[2295] == INFINITY) ? NAN : history[2295]);
        }
        if (history[2296] == 0){
            out[1130] = NAN;
        } else {
            temp_mean = history[2297]/history[2296];
            out[1130] = sqrt((
                history[2298] - pow(temp_mean, 2) * history[2296]
            )/(history[2296]-1));
        }
        if (history[2299] == 0){
            out[1131] = NAN;
        } else {
            out[1131] = history[2300];
        }
        if (history[2301] == 0){
            out[1132] = NAN;
        } else {
            temp = ((history[2302] == -INFINITY) ? NAN : history[2302]);
            out[1132] = temp;
        }
        if (history[2303] == 0){
            out[1133] = NAN;
        } else {
            temp = ((history[2304] == -INFINITY) ? NAN : history[2304]);
            out[1133] = temp;
        }
        if (history[2305] == 0){
            out[1134] = NAN;
        } else {
            temp_mean = history[2306]/history[2305];
            out[1134] = sqrt((
                history[2307] - pow(temp_mean, 2) * history[2305]
            )/(history[2305]-1));
        }
        if (history[2308] == 0){
            out[1135] = NAN;
        } else {
            out[1135] = history[2309];
        }
        if (history[2310] == 0){
            out[1136] = NAN;
        } else {
            temp = ((history[2311] == -INFINITY) ? NAN : history[2311]);
            out[1136] = temp;
        }
        if (history[2312] == 0){
            out[1137] = NAN;
        } else {
            temp = ((history[2313] == -INFINITY) ? NAN : history[2313]);
            out[1137] = temp;
        }
        if (history[2314] == 0){
            out[1138] = NAN;
        } else {
            out[1138] = history[2315]/history[2314];
        }
        if (history[2316] == 0){
            out[1139] = NAN;
        } else {
            out[1139] = history[2317]/history[2316];
        }
        if (history[2318] == 0){
            out[1140] = NAN;
        } else {
            out[1140] = ((history[2319] == INFINITY) ? NAN : history[2319]);
        }
        if (history[2320] == 0){
            out[1141] = NAN;
        } else {
            out[1141] = ((history[2321] == INFINITY) ? NAN : history[2321]);
        }
        if (history[2322] == 0){
            out[1142] = NAN;
        } else {
            out[1142] = ((history[2323] == INFINITY) ? NAN : history[2323]);
        }
        if (history[2324] == 0){
            out[1143] = NAN;
        } else {
            out[1143] = ((history[2325] == INFINITY) ? NAN : history[2325]);
        }
        if (history[2326] == 0){
            out[1144] = NAN;
        } else {
            out[1144] = ((history[2327] == INFINITY) ? NAN : history[2327]);
        }
        if (history[2328] == 0){
            out[1145] = NAN;
        } else {
            temp_mean = history[2329]/history[2328];
            out[1145] = sqrt((
                history[2330] - pow(temp_mean, 2) * history[2328]
            )/(history[2328]-1));
        }
        if (history[2331] == 0){
            out[1146] = NAN;
        } else {
            out[1146] = ((history[2332] == INFINITY) ? NAN : history[2332]);
        }
        if (history[2333] == 0){
            out[1147] = NAN;
        } else {
            out[1147] = ((history[2334] == INFINITY) ? NAN : history[2334]);
        }
        if (history[2335] == 0){
            out[1148] = NAN;
        } else {
            out[1148] = ((history[2336] == INFINITY) ? NAN : history[2336]);
        }
        if (history[2337] == 0){
            out[1149] = NAN;
        } else {
            out[1149] = history[2338];
        }
        if (history[2339] == 0){
            out[1150] = NAN;
        } else {
            temp = ((history[2340] == -INFINITY) ? NAN : history[2340]);
            out[1150] = temp;
        }
        if (history[2341] == 0){
            out[1151] = NAN;
        } else {
            temp = ((history[2342] == -INFINITY) ? NAN : history[2342]);
            out[1151] = temp;
        }
        if (history[2343] == 0){
            out[1152] = NAN;
        } else {
            temp = ((history[2344] == -INFINITY) ? NAN : history[2344]);
            out[1152] = temp;
        }
        if (history[2345] == 0){
            out[1153] = NAN;
        } else {
            temp_mean = history[2346]/history[2345];
            out[1153] = sqrt((
                history[2347] - pow(temp_mean, 2) * history[2345]
            )/(history[2345]-1));
        }
        if (history[2348] == 0){
            out[1154] = NAN;
        } else {
            temp_mean = history[2349]/history[2348];
            out[1154] = sqrt((
                history[2350] - pow(temp_mean, 2) * history[2348]
            )/(history[2348]-1));
        }
        if (history[2351] == 0){
            out[1155] = NAN;
        } else {
            out[1155] = history[2352];
        }
        if (history[2353] == 0){
            out[1156] = NAN;
        } else {
            out[1156] = history[2354];
        }
        if (history[2355] == 0){
            out[1157] = NAN;
        } else {
            temp = ((history[2356] == -INFINITY) ? NAN : history[2356]);
            out[1157] = temp;
        }
        if (history[2357] == 0){
            out[1158] = NAN;
        } else {
            temp = ((history[2358] == -INFINITY) ? NAN : history[2358]);
            out[1158] = temp;
        }
        if (history[2359] == 0){
            out[1159] = NAN;
        } else {
            out[1159] = history[2360]/history[2359];
        }
        if (history[2361] == 0){
            out[1160] = NAN;
        } else {
            out[1160] = ((history[2362] == INFINITY) ? NAN : history[2362]);
        }
        if (history[2363] == 0){
            out[1161] = NAN;
        } else {
            out[1161] = ((history[2364] == INFINITY) ? NAN : history[2364]);
        }
        if (history[2365] == 0){
            out[1162] = NAN;
        } else {
            temp_mean = history[2366]/history[2365];
            out[1162] = sqrt((
                history[2367] - pow(temp_mean, 2) * history[2365]
            )/(history[2365]-1));
        }
        if (history[2368] == 0){
            out[1163] = NAN;
        } else {
            temp_mean = history[2369]/history[2368];
            out[1163] = sqrt((
                history[2370] - pow(temp_mean, 2) * history[2368]
            )/(history[2368]-1));
        }
        if (history[2371] == 0){
            out[1164] = NAN;
        } else {
            temp_mean = history[2372]/history[2371];
            out[1164] = sqrt((
                history[2373] - pow(temp_mean, 2) * history[2371]
            )/(history[2371]-1));
        }
            out[1165] = history[2264] - history[858];
            out[1166] = history[2389] - history[926];
            out[1167] = history[2266] - history[951];
            out[1168] = history[2391] - history[949];
            out[1169] = history[2252] - history[929];
            out[1170] = history[2254] - history[903];
        if (history[2374] == 0){
            out[1171] = NAN;
        } else {
            temp_mean = history[2375]/history[2374];
            out[1171] = sqrt((
                history[2376] - pow(temp_mean, 2) * history[2374]
            )/(history[2374]-1));
        }
        if (history[2377] == 0){
            out[1172] = NAN;
        } else {
            temp_mean = history[2378]/history[2377];
            out[1172] = sqrt((
                history[2379] - pow(temp_mean, 2) * history[2377]
            )/(history[2377]-1));
        }
        if (history[2380] == 0){
            out[1173] = NAN;
        } else {
            temp_mean = history[2381]/history[2380];
            out[1173] = sqrt((
                history[2382] - pow(temp_mean, 2) * history[2380]
            )/(history[2380]-1));
        }
        if (history[2383] == 0){
            out[1174] = NAN;
        } else {
            temp_mean = history[2384]/history[2383];
            out[1174] = sqrt((
                history[2385] - pow(temp_mean, 2) * history[2383]
            )/(history[2383]-1));
        }
            out[1175] = history[2393] - history[856];
            out[1176] = history[2262] - history[861];
            out[1177] = history[2268] - history[861];
            out[1178] = history[2278] - history[876];
            out[1179] = history[2399] - history[876];
            out[1180] = history[2274] - history[916];
            out[1181] = history[2395] - history[916];
            out[1182] = history[2401] - history[916];
            out[1183] = history[2270] - history[924];
            out[1184] = history[2387] - history[924];
            out[1185] = history[2256] - history[905];
            out[1186] = history[2258] - history[900];
            out[1187] = history[2280] - history[900];
            out[1188] = history[2397] - history[900];
            out[1189] = history[2260] - history[956];
            out[1190] = history[2272] - history[939];
            out[1191] = history[2276] - history[906];
        if (history[2420] == 0){
            out[1192] = NAN;
        } else {
            temp = ((history[2421] == -INFINITY) ? NAN : history[2421]);
            out[1192] = temp;
        }
        if (history[2422] == 0){
            out[1193] = NAN;
        } else {
            temp_mean = history[2423]/history[2422];
            out[1193] = sqrt((
                history[2424] - pow(temp_mean, 2) * history[2422]
            )/(history[2422]-1));
        }
        if (history[2425] == 0){
            out[1194] = NAN;
        } else {
            temp_mean = history[2426]/history[2425];
            out[1194] = sqrt((
                history[2427] - pow(temp_mean, 2) * history[2425]
            )/(history[2425]-1));
        }
        if (history[2428] == 0){
            out[1195] = NAN;
        } else {
            temp = ((history[2429] == -INFINITY) ? NAN : history[2429]);
            out[1195] = temp;
        }
        if (history[2430] == 0){
            out[1196] = NAN;
        } else {
            out[1196] = history[2431]/history[2430];
        }
        if (history[2432] == 0){
            out[1197] = NAN;
        } else {
            out[1197] = history[2433];
        }
        if (history[2434] == 0){
            out[1198] = NAN;
        } else {
            out[1198] = history[2435]/history[2434];
        }
        if (history[2436] == 0){
            out[1199] = NAN;
        } else {
            out[1199] = history[2437];
        }
        if (history[2438] == 0){
            out[1200] = NAN;
        } else {
            temp = ((history[2439] == -INFINITY) ? NAN : history[2439]);
            out[1200] = temp;
        }
        if (history[2440] == 0){
            out[1201] = NAN;
        } else {
            temp_mean = history[2441]/history[2440];
            out[1201] = sqrt((
                history[2442] - pow(temp_mean, 2) * history[2440]
            )/(history[2440]-1));
        }
        if (history[2443] == 0){
            out[1202] = NAN;
        } else {
            out[1202] = history[2444];
        }
            out[1203] = history[2497] - history[1084];
            out[1204] = history[2419] - history[1084];
            out[1205] = history[2499] - history[1029];
            out[1206] = history[2485] - history[980];
        if (history[2445] == 0){
            out[1207] = NAN;
        } else {
            temp = ((history[2446] == -INFINITY) ? NAN : history[2446]);
            out[1207] = temp;
        }
        if (history[2447] == 0){
            out[1208] = NAN;
        } else {
            out[1208] = ((history[2448] == INFINITY) ? NAN : history[2448]);
        }
        if (history[2449] == 0){
            out[1209] = NAN;
        } else {
            out[1209] = ((history[2450] == INFINITY) ? NAN : history[2450]);
        }
        if (history[2451] == 0){
            out[1210] = NAN;
        } else {
            out[1210] = history[2452];
        }
        if (history[2453] == 0){
            out[1211] = NAN;
        } else {
            temp = ((history[2454] == -INFINITY) ? NAN : history[2454]);
            out[1211] = temp;
        }
        if (history[2455] == 0){
            out[1212] = NAN;
        } else {
            temp = ((history[2456] == -INFINITY) ? NAN : history[2456]);
            out[1212] = temp;
        }
        if (history[2457] == 0){
            out[1213] = NAN;
        } else {
            out[1213] = history[2458]/history[2457];
        }
        if (history[2459] == 0){
            out[1214] = NAN;
        } else {
            out[1214] = history[2460]/history[2459];
        }
        if (history[2461] == 0){
            out[1215] = NAN;
        } else {
            temp_mean = history[2462]/history[2461];
            out[1215] = sqrt((
                history[2463] - pow(temp_mean, 2) * history[2461]
            )/(history[2461]-1));
        }
        if (history[2464] == 0){
            out[1216] = NAN;
        } else {
            out[1216] = history[2465];
        }
        if (history[2466] == 0){
            out[1217] = NAN;
        } else {
            temp = ((history[2467] == -INFINITY) ? NAN : history[2467]);
            out[1217] = temp;
        }
        if (history[2468] == 0){
            out[1218] = NAN;
        } else {
            out[1218] = history[2469];
        }
        if (history[2470] == 0){
            out[1219] = NAN;
        } else {
            out[1219] = history[2471]/history[2470];
        }
        if (history[2472] == 0){
            out[1220] = NAN;
        } else {
            out[1220] = history[2473]/history[2472];
        }
        if (history[2474] == 0){
            out[1221] = NAN;
        } else {
            out[1221] = history[2475]/history[2474];
        }
        if (history[2476] == 0){
            out[1222] = NAN;
        } else {
            out[1222] = history[2477];
        }
            out[1223] = history[2491] - history[1075];
            out[1224] = history[2493] - history[1031];
            out[1225] = history[2483] - history[1037];
            out[1226] = history[2481] - history[1019];
            out[1227] = history[2407] - history[1041];
            out[1228] = history[2415] - history[1045];
            out[1229] = history[2403] - history[1086];
            out[1230] = history[2413] - history[1058];
            out[1231] = history[2495] - history[997];
            out[1232] = history[2479] - history[997];
            out[1233] = history[2487] - history[1001];
            out[1234] = history[2409] - history[1005];
            out[1235] = history[2489] - history[1064];
            out[1236] = history[2411] - history[1064];
            out[1237] = history[2405] - history[1032];
            out[1238] = history[2417] - history[988];
        if (history[1089] == 0){
            out[1239] = NAN;
        } else {
            temp = ((history[1090] == -INFINITY) ? NAN : history[1090]);
            out[1239] = temp;
        }
        if (history[1089] == 0){
            out[1240] = NAN;
        } else {
            temp_mean = history[1091]/history[1089];
            out[1240] = sqrt((
                history[1092] - pow(temp_mean, 2) * history[1089]
            )/(history[1089]-1));
        }
        if (history[2571] == 0){
            out[1241] = NAN;
        } else {
            temp = ((history[2572] == -INFINITY) ? NAN : history[2572]);
            out[1241] = temp;
        }
        if (history[2573] == 0){
            out[1242] = NAN;
        } else {
            out[1242] = history[2574]/history[2573];
        }
        if (history[2575] == 0){
            out[1243] = NAN;
        } else {
            temp = ((history[2576] == -INFINITY) ? NAN : history[2576]);
            out[1243] = temp;
        }
        if (history[2577] == 0){
            out[1244] = NAN;
        } else {
            out[1244] = history[2578];
        }
        if (history[2579] == 0){
            out[1245] = NAN;
        } else {
            temp = ((history[2580] == -INFINITY) ? NAN : history[2580]);
            out[1245] = temp;
        }
        if (history[2581] == 0){
            out[1246] = NAN;
        } else {
            temp = ((history[2582] == -INFINITY) ? NAN : history[2582]);
            out[1246] = temp;
        }
        if (history[2583] == 0){
            out[1247] = NAN;
        } else {
            temp = ((history[2584] == -INFINITY) ? NAN : history[2584]);
            out[1247] = temp;
        }
        if (history[2585] == 0){
            out[1248] = NAN;
        } else {
            temp = ((history[2586] == -INFINITY) ? NAN : history[2586]);
            out[1248] = temp;
        }
        if (history[2587] == 0){
            out[1249] = NAN;
        } else {
            out[1249] = history[2588];
        }
        if (history[2589] == 0){
            out[1250] = NAN;
        } else {
            out[1250] = history[2590]/history[2589];
        }
        if (history[2591] == 0){
            out[1251] = NAN;
        } else {
            out[1251] = history[2592]/history[2591];
        }
        if (history[2593] == 0){
            out[1252] = NAN;
        } else {
            out[1252] = history[2594];
        }
        if (history[2595] == 0){
            out[1253] = NAN;
        } else {
            temp_mean = history[2596]/history[2595];
            out[1253] = sqrt((
                history[2597] - pow(temp_mean, 2) * history[2595]
            )/(history[2595]-1));
        }
        if (history[2598] == 0){
            out[1254] = NAN;
        } else {
            temp_mean = history[2599]/history[2598];
            out[1254] = sqrt((
                history[2600] - pow(temp_mean, 2) * history[2598]
            )/(history[2598]-1));
        }
        if (history[2601] == 0){
            out[1255] = NAN;
        } else {
            temp_mean = history[2602]/history[2601];
            out[1255] = sqrt((
                history[2603] - pow(temp_mean, 2) * history[2601]
            )/(history[2601]-1));
        }
        if (history[2604] == 0){
            out[1256] = NAN;
        } else {
            temp_mean = history[2605]/history[2604];
            out[1256] = sqrt((
                history[2606] - pow(temp_mean, 2) * history[2604]
            )/(history[2604]-1));
        }
        if (history[2607] == 0){
            out[1257] = NAN;
        } else {
            out[1257] = history[2608];
        }
        if (history[2609] == 0){
            out[1258] = NAN;
        } else {
            out[1258] = history[2610];
        }
        if (history[2611] == 0){
            out[1259] = NAN;
        } else {
            out[1259] = history[2612];
        }
        if (history[2613] == 0){
            out[1260] = NAN;
        } else {
            temp = ((history[2614] == -INFINITY) ? NAN : history[2614]);
            out[1260] = temp;
        }
        if (history[2615] == 0){
            out[1261] = NAN;
        } else {
            out[1261] = history[2616]/history[2615];
        }
        if (history[2617] == 0){
            out[1262] = NAN;
        } else {
            out[1262] = history[2618];
        }
        if (history[2619] == 0){
            out[1263] = NAN;
        } else {
            out[1263] = history[2620];
        }
        if (history[2621] == 0){
            out[1264] = NAN;
        } else {
            temp = ((history[2622] == -INFINITY) ? NAN : history[2622]);
            out[1264] = temp;
        }
        if (history[2623] == 0){
            out[1265] = NAN;
        } else {
            temp = ((history[2624] == -INFINITY) ? NAN : history[2624]);
            out[1265] = temp;
        }
        if (history[2625] == 0){
            out[1266] = NAN;
        } else {
            temp = ((history[2626] == -INFINITY) ? NAN : history[2626]);
            out[1266] = temp;
        }
        if (history[2627] == 0){
            out[1267] = NAN;
        } else {
            temp = ((history[2628] == -INFINITY) ? NAN : history[2628]);
            out[1267] = temp;
        }
        if (history[2629] == 0){
            out[1268] = NAN;
        } else {
            temp = ((history[2630] == -INFINITY) ? NAN : history[2630]);
            out[1268] = temp;
        }
        if (history[2631] == 0){
            out[1269] = NAN;
        } else {
            out[1269] = ((history[2632] == INFINITY) ? NAN : history[2632]);
        }
        if (history[2633] == 0){
            out[1270] = NAN;
        } else {
            out[1270] = ((history[2634] == INFINITY) ? NAN : history[2634]);
        }
        if (history[2635] == 0){
            out[1271] = NAN;
        } else {
            temp = ((history[2636] == -INFINITY) ? NAN : history[2636]);
            out[1271] = temp;
        }
        if (history[2637] == 0){
            out[1272] = NAN;
        } else {
            temp = ((history[2638] == -INFINITY) ? NAN : history[2638]);
            out[1272] = temp;
        }
        if (history[2639] == 0){
            out[1273] = NAN;
        } else {
            out[1273] = history[2640]/history[2639];
        }
        if (history[2641] == 0){
            out[1274] = NAN;
        } else {
            out[1274] = ((history[2642] == INFINITY) ? NAN : history[2642]);
        }
        if (history[2643] == 0){
            out[1275] = NAN;
        } else {
            out[1275] = ((history[2644] == INFINITY) ? NAN : history[2644]);
        }
        if (history[2645] == 0){
            out[1276] = NAN;
        } else {
            temp_mean = history[2646]/history[2645];
            out[1276] = sqrt((
                history[2647] - pow(temp_mean, 2) * history[2645]
            )/(history[2645]-1));
        }
        if (history[2648] == 0){
            out[1277] = NAN;
        } else {
            temp = ((history[2649] == -INFINITY) ? NAN : history[2649]);
            out[1277] = temp;
        }
        if (history[2650] == 0){
            out[1278] = NAN;
        } else {
            temp = ((history[2651] == -INFINITY) ? NAN : history[2651]);
            out[1278] = temp;
        }
        if (history[2652] == 0){
            out[1279] = NAN;
        } else {
            temp = ((history[2653] == -INFINITY) ? NAN : history[2653]);
            out[1279] = temp;
        }
        if (history[2654] == 0){
            out[1280] = NAN;
        } else {
            out[1280] = history[2655]/history[2654];
        }
        if (history[2656] == 0){
            out[1281] = NAN;
        } else {
            out[1281] = history[2657]/history[2656];
        }
        if (history[2658] == 0){
            out[1282] = NAN;
        } else {
            out[1282] = history[2659]/history[2658];
        }
        if (history[2660] == 0){
            out[1283] = NAN;
        } else {
            out[1283] = ((history[2661] == INFINITY) ? NAN : history[2661]);
        }
        if (history[2662] == 0){
            out[1284] = NAN;
        } else {
            temp_mean = history[2663]/history[2662];
            out[1284] = sqrt((
                history[2664] - pow(temp_mean, 2) * history[2662]
            )/(history[2662]-1));
        }
        if (history[2665] == 0){
            out[1285] = NAN;
        } else {
            temp_mean = history[2666]/history[2665];
            out[1285] = sqrt((
                history[2667] - pow(temp_mean, 2) * history[2665]
            )/(history[2665]-1));
        }
        if (history[2668] == 0){
            out[1286] = NAN;
        } else {
            temp_mean = history[2669]/history[2668];
            out[1286] = sqrt((
                history[2670] - pow(temp_mean, 2) * history[2668]
            )/(history[2668]-1));
        }
        if (history[2671] == 0){
            out[1287] = NAN;
        } else {
            temp_mean = history[2672]/history[2671];
            out[1287] = sqrt((
                history[2673] - pow(temp_mean, 2) * history[2671]
            )/(history[2671]-1));
        }
        if (history[2674] == 0){
            out[1288] = NAN;
        } else {
            out[1288] = history[2675];
        }
        if (history[2676] == 0){
            out[1289] = NAN;
        } else {
            temp = ((history[2677] == -INFINITY) ? NAN : history[2677]);
            out[1289] = temp;
        }
        if (history[2678] == 0){
            out[1290] = NAN;
        } else {
            temp = ((history[2679] == -INFINITY) ? NAN : history[2679]);
            out[1290] = temp;
        }
        if (history[2680] == 0){
            out[1291] = NAN;
        } else {
            temp = ((history[2681] == -INFINITY) ? NAN : history[2681]);
            out[1291] = temp;
        }
        if (history[2682] == 0){
            out[1292] = NAN;
        } else {
            temp_mean = history[2683]/history[2682];
            out[1292] = sqrt((
                history[2684] - pow(temp_mean, 2) * history[2682]
            )/(history[2682]-1));
        }
        if (history[2685] == 0){
            out[1293] = NAN;
        } else {
            temp_mean = history[2686]/history[2685];
            out[1293] = sqrt((
                history[2687] - pow(temp_mean, 2) * history[2685]
            )/(history[2685]-1));
        }
        if (history[2688] == 0){
            out[1294] = NAN;
        } else {
            out[1294] = history[2689]/history[2688];
        }
            out[1295] = history[2501] - history[1221];
            out[1296] = history[2701] - history[1221];
            out[1297] = history[2707] - history[1232];
            out[1298] = history[2697] - history[1213];
            out[1299] = history[2715] - history[1099];
            out[1300] = history[2562] - history[1110];
            out[1301] = history[2709] - history[1138];
            out[1302] = history[2530] - history[1138];
            out[1303] = history[2711] - history[1107];
            out[1304] = history[2733] - history[1120];
            out[1305] = history[2725] - history[1155];
            out[1306] = history[2546] - history[1202];
            out[1307] = history[2503] - history[1222];
            out[1308] = history[2505] - history[1233];
            out[1309] = history[2717] - history[1230];
            out[1310] = history[2719] - history[1139];
            out[1311] = history[2534] - history[1139];
            out[1312] = history[2507] - history[1139];
            out[1313] = history[2554] - history[1139];
            out[1314] = history[2693] - history[1139];
            out[1315] = history[2517] - history[1121];
            out[1316] = history[2727] - history[1121];
            out[1317] = history[2519] - history[1121];
            out[1318] = history[2521] - history[1153];
            out[1319] = history[2721] - history[1136];
            out[1320] = history[2729] - history[1136];
            out[1321] = history[2564] - history[1136];
            out[1322] = history[2509] - history[1171];
            out[1323] = history[2523] - history[1235];
            out[1324] = history[2556] - history[1235];
            out[1325] = history[2524] - history[1235];
            out[1326] = history[2570] - history[1235];
            out[1327] = history[2739] - history[1238];
            out[1328] = history[2558] - history[1238];
            out[1329] = history[2536] - history[1227];
            out[1330] = history[2542] - history[1219];
            out[1331] = history[2741] - history[1132];
            out[1332] = history[2538] - history[1102];
            out[1333] = history[2723] - history[1113];
            out[1334] = history[2550] - history[1113];
            out[1335] = history[2511] - history[1097];
            out[1336] = history[2713] - history[1147];
            out[1337] = history[2735] - history[1149];
            out[1338] = history[2737] - history[1149];
            out[1339] = history[2552] - history[1165];
            out[1340] = history[2526] - history[1165];
            out[1341] = history[2513] - history[1176];
            out[1342] = history[2528] - history[1181];
            out[1343] = history[2566] - history[1181];
            out[1344] = history[2548] - history[1204];
            out[1345] = history[2703] - history[1193];
            out[1346] = history[2544] - history[1193];
            out[1347] = history[2695] - history[1236];
            out[1348] = history[2540] - history[1141];
            out[1349] = history[2532] - history[1141];
            out[1350] = history[2515] - history[1141];
            out[1351] = history[2699] - history[1141];
            out[1352] = history[2731] - history[1123];
            out[1353] = history[2568] - history[1150];
            out[1354] = history[2691] - history[1150];
            out[1355] = history[2560] - history[1160];
            out[1356] = history[2705] - history[1194];
        out[1357] = history[1172];
        if (history[2744] == 0){
            out[1358] = NAN;
        } else {
            temp = ((history[2745] == -INFINITY) ? NAN : history[2745]);
            out[1358] = temp;
        }
        if (history[2746] == 0){
            out[1359] = NAN;
        } else {
            out[1359] = history[2747];
        }
        if (history[2748] == 0){
            out[1360] = NAN;
        } else {
            temp = ((history[2749] == -INFINITY) ? NAN : history[2749]);
            out[1360] = temp;
        }
        if (history[2750] == 0){
            out[1361] = NAN;
        } else {
            out[1361] = history[2751]/history[2750];
        }
        if (history[2752] == 0){
            out[1362] = NAN;
        } else {
            out[1362] = history[2753]/history[2752];
        }
        if (history[2754] == 0){
            out[1363] = NAN;
        } else {
            temp_mean = history[2755]/history[2754];
            out[1363] = sqrt((
                history[2756] - pow(temp_mean, 2) * history[2754]
            )/(history[2754]-1));
        }
        if (history[2757] == 0){
            out[1364] = NAN;
        } else {
            out[1364] = history[2758];
        }
        if (history[2759] == 0){
            out[1365] = NAN;
        } else {
            temp = ((history[2760] == -INFINITY) ? NAN : history[2760]);
            out[1365] = temp;
        }
        if (history[2761] == 0){
            out[1366] = NAN;
        } else {
            out[1366] = history[2762];
        }
        if (history[2763] == 0){
            out[1367] = NAN;
        } else {
            out[1367] = history[2764];
        }
        if (history[2765] == 0){
            out[1368] = NAN;
        } else {
            temp = ((history[2766] == -INFINITY) ? NAN : history[2766]);
            out[1368] = temp;
        }
        if (history[2767] == 0){
            out[1369] = NAN;
        } else {
            temp = ((history[2768] == -INFINITY) ? NAN : history[2768]);
            out[1369] = temp;
        }
        if (history[2769] == 0){
            out[1370] = NAN;
        } else {
            out[1370] = ((history[2770] == INFINITY) ? NAN : history[2770]);
        }
        if (history[2771] == 0){
            out[1371] = NAN;
        } else {
            out[1371] = history[2772];
        }
        if (history[2773] == 0){
            out[1372] = NAN;
        } else {
            out[1372] = history[2774];
        }
        if (history[2775] == 0){
            out[1373] = NAN;
        } else {
            out[1373] = history[2776];
        }
            out[1374] = history[2782] - history[1247];
            out[1375] = history[2778] - history[1255];
            out[1376] = history[2788] - history[1279];
            out[1377] = history[2743] - history[1279];
            out[1378] = history[2789] - history[1279];
            out[1379] = history[2780] - history[1286];
            out[1380] = history[2784] - history[1270];
            out[1381] = history[2786] - history[1297];
        if (history[1300] == 0){
            out[1382] = NAN;
        } else {
            temp = ((history[1301] == -INFINITY) ? NAN : history[1301]);
            out[1382] = temp;
        }
        if (history[2812] == 0){
            out[1383] = NAN;
        } else {
            temp = ((history[2813] == -INFINITY) ? NAN : history[2813]);
            out[1383] = temp;
        }
        if (history[2814] == 0){
            out[1384] = NAN;
        } else {
            out[1384] = ((history[2815] == INFINITY) ? NAN : history[2815]);
        }
        if (history[2816] == 0){
            out[1385] = NAN;
        } else {
            temp = ((history[2817] == -INFINITY) ? NAN : history[2817]);
            out[1385] = temp;
        }
        if (history[2818] == 0){
            out[1386] = NAN;
        } else {
            temp = ((history[2819] == -INFINITY) ? NAN : history[2819]);
            out[1386] = temp;
        }
        if (history[2820] == 0){
            out[1387] = NAN;
        } else {
            temp = ((history[2821] == -INFINITY) ? NAN : history[2821]);
            out[1387] = temp;
        }
        if (history[2822] == 0){
            out[1388] = NAN;
        } else {
            temp = ((history[2823] == -INFINITY) ? NAN : history[2823]);
            out[1388] = temp;
        }
        if (history[2824] == 0){
            out[1389] = NAN;
        } else {
            temp = ((history[2825] == -INFINITY) ? NAN : history[2825]);
            out[1389] = temp;
        }
        if (history[2826] == 0){
            out[1390] = NAN;
        } else {
            out[1390] = history[2827]/history[2826];
        }
        if (history[2828] == 0){
            out[1391] = NAN;
        } else {
            temp_mean = history[2829]/history[2828];
            out[1391] = sqrt((
                history[2830] - pow(temp_mean, 2) * history[2828]
            )/(history[2828]-1));
        }
        if (history[2831] == 0){
            out[1392] = NAN;
        } else {
            temp_mean = history[2832]/history[2831];
            out[1392] = sqrt((
                history[2833] - pow(temp_mean, 2) * history[2831]
            )/(history[2831]-1));
        }
        if (history[2834] == 0){
            out[1393] = NAN;
        } else {
            temp_mean = history[2835]/history[2834];
            out[1393] = sqrt((
                history[2836] - pow(temp_mean, 2) * history[2834]
            )/(history[2834]-1));
        }
        if (history[2837] == 0){
            out[1394] = NAN;
        } else {
            temp = ((history[2838] == -INFINITY) ? NAN : history[2838]);
            out[1394] = temp;
        }
        if (history[2839] == 0){
            out[1395] = NAN;
        } else {
            temp = ((history[2840] == -INFINITY) ? NAN : history[2840]);
            out[1395] = temp;
        }
        if (history[2841] == 0){
            out[1396] = NAN;
        } else {
            temp = ((history[2842] == -INFINITY) ? NAN : history[2842]);
            out[1396] = temp;
        }
        if (history[2843] == 0){
            out[1397] = NAN;
        } else {
            out[1397] = history[2844];
        }
            out[1398] = history[2793] - history[1345];
            out[1399] = history[2885] - history[1349];
            out[1400] = history[2803] - history[1346];
            out[1401] = history[2795] - history[1313];
            out[1402] = history[2797] - history[1335];
            out[1403] = history[2875] - history[1376];
        if (history[2845] == 0){
            out[1404] = NAN;
        } else {
            temp = ((history[2846] == -INFINITY) ? NAN : history[2846]);
            out[1404] = temp;
        }
        if (history[2847] == 0){
            out[1405] = NAN;
        } else {
            out[1405] = history[2848]/history[2847];
        }
        if (history[2849] == 0){
            out[1406] = NAN;
        } else {
            out[1406] = ((history[2850] == INFINITY) ? NAN : history[2850]);
        }
        if (history[2851] == 0){
            out[1407] = NAN;
        } else {
            temp_mean = history[2852]/history[2851];
            out[1407] = sqrt((
                history[2853] - pow(temp_mean, 2) * history[2851]
            )/(history[2851]-1));
        }
        if (history[2854] == 0){
            out[1408] = NAN;
        } else {
            out[1408] = history[2855];
        }
        if (history[2856] == 0){
            out[1409] = NAN;
        } else {
            temp = ((history[2857] == -INFINITY) ? NAN : history[2857]);
            out[1409] = temp;
        }
        if (history[2858] == 0){
            out[1410] = NAN;
        } else {
            out[1410] = history[2859];
        }
        if (history[2860] == 0){
            out[1411] = NAN;
        } else {
            temp = ((history[2861] == -INFINITY) ? NAN : history[2861]);
            out[1411] = temp;
        }
        if (history[2862] == 0){
            out[1412] = NAN;
        } else {
            temp = ((history[2863] == -INFINITY) ? NAN : history[2863]);
            out[1412] = temp;
        }
        if (history[2864] == 0){
            out[1413] = NAN;
        } else {
            out[1413] = history[2865];
        }
        if (history[2866] == 0){
            out[1414] = NAN;
        } else {
            out[1414] = history[2867];
        }
        if (history[2868] == 0){
            out[1415] = NAN;
        } else {
            out[1415] = ((history[2869] == INFINITY) ? NAN : history[2869]);
        }
        if (history[2870] == 0){
            out[1416] = NAN;
        } else {
            out[1416] = history[2871];
        }
            out[1417] = history[2881] - history[1356];
            out[1418] = history[2887] - history[1343];
            out[1419] = history[2799] - history[1332];
            out[1420] = history[2807] - history[1308];
            out[1421] = history[2873] - history[1391];
            out[1422] = history[2877] - history[1386];
            out[1423] = history[2809] - history[1372];
            out[1424] = history[2805] - history[1380];
            out[1425] = history[2811] - history[1357];
            out[1426] = history[2791] - history[1333];
            out[1427] = history[2879] - history[1378];
            out[1428] = history[2883] - history[1373];
            out[1429] = history[2801] - history[1373];
        if (history[2898] == 0){
            out[1430] = NAN;
        } else {
            temp = ((history[2899] == -INFINITY) ? NAN : history[2899]);
            out[1430] = temp;
        }
        if (history[2900] == 0){
            out[1431] = NAN;
        } else {
            temp_mean = history[2901]/history[2900];
            out[1431] = sqrt((
                history[2902] - pow(temp_mean, 2) * history[2900]
            )/(history[2900]-1));
        }
        if (history[2903] == 0){
            out[1432] = NAN;
        } else {
            temp_mean = history[2904]/history[2903];
            out[1432] = sqrt((
                history[2905] - pow(temp_mean, 2) * history[2903]
            )/(history[2903]-1));
        }
        if (history[2906] == 0){
            out[1433] = NAN;
        } else {
            out[1433] = history[2907]/history[2906];
        }
        if (history[2908] == 0){
            out[1434] = NAN;
        } else {
            out[1434] = history[2909]/history[2908];
        }
        if (history[2910] == 0){
            out[1435] = NAN;
        } else {
            out[1435] = history[2911];
        }
        if (history[2912] == 0){
            out[1436] = NAN;
        } else {
            out[1436] = history[2913];
        }
        if (history[2914] == 0){
            out[1437] = NAN;
        } else {
            out[1437] = history[2915]/history[2914];
        }
        if (history[2916] == 0){
            out[1438] = NAN;
        } else {
            out[1438] = history[2917]/history[2916];
        }
        if (history[2918] == 0){
            out[1439] = NAN;
        } else {
            temp_mean = history[2919]/history[2918];
            out[1439] = sqrt((
                history[2920] - pow(temp_mean, 2) * history[2918]
            )/(history[2918]-1));
        }
        if (history[2921] == 0){
            out[1440] = NAN;
        } else {
            out[1440] = history[2922];
        }
        if (history[2923] == 0){
            out[1441] = NAN;
        } else {
            out[1441] = history[2924]/history[2923];
        }
        if (history[2925] == 0){
            out[1442] = NAN;
        } else {
            out[1442] = ((history[2926] == INFINITY) ? NAN : history[2926]);
        }
        if (history[2927] == 0){
            out[1443] = NAN;
        } else {
            temp_mean = history[2928]/history[2927];
            out[1443] = sqrt((
                history[2929] - pow(temp_mean, 2) * history[2927]
            )/(history[2927]-1));
        }
        if (history[2930] == 0){
            out[1444] = NAN;
        } else {
            temp_mean = history[2931]/history[2930];
            out[1444] = sqrt((
                history[2932] - pow(temp_mean, 2) * history[2930]
            )/(history[2930]-1));
        }
        if (history[2933] == 0){
            out[1445] = NAN;
        } else {
            temp_mean = history[2934]/history[2933];
            out[1445] = sqrt((
                history[2935] - pow(temp_mean, 2) * history[2933]
            )/(history[2933]-1));
        }
        if (history[2936] == 0){
            out[1446] = NAN;
        } else {
            out[1446] = history[2937];
        }
        if (history[2938] == 0){
            out[1447] = NAN;
        } else {
            out[1447] = history[2939];
        }
        if (history[2940] == 0){
            out[1448] = NAN;
        } else {
            out[1448] = ((history[2941] == INFINITY) ? NAN : history[2941]);
        }
        if (history[2942] == 0){
            out[1449] = NAN;
        } else {
            out[1449] = history[2943];
        }
            out[1450] = history[2947] - history[1458];
            out[1451] = history[2889] - history[1458];
            out[1452] = history[2945] - history[1462];
            out[1453] = history[2895] - history[1454];
            out[1454] = history[2891] - history[1447];
            out[1455] = history[2893] - history[1414];
            out[1456] = history[2957] - history[1474];
            out[1457] = history[2953] - history[1469];
            out[1458] = history[2955] - history[1432];
            out[1459] = history[2949] - history[1434];
            out[1460] = history[2897] - history[1427];
            out[1461] = history[2951] - history[1478];
        if (history[1481] == 0){
            out[1462] = NAN;
        } else {
            out[1462] = history[1482];
        }
        if (history[1481] == 0){
            out[1463] = NAN;
        } else {
            temp_mean = history[1482]/history[1481];
            out[1463] = sqrt((
                history[1483] - pow(temp_mean, 2) * history[1481]
            )/(history[1481]-1));
        }
        if (history[2988] == 0){
            out[1464] = NAN;
        } else {
            temp = ((history[2989] == -INFINITY) ? NAN : history[2989]);
            out[1464] = temp;
        }
        if (history[2990] == 0){
            out[1465] = NAN;
        } else {
            out[1465] = history[2991]/history[2990];
        }
        if (history[2992] == 0){
            out[1466] = NAN;
        } else {
            temp = ((history[2993] == -INFINITY) ? NAN : history[2993]);
            out[1466] = temp;
        }
        if (history[2994] == 0){
            out[1467] = NAN;
        } else {
            temp = ((history[2995] == -INFINITY) ? NAN : history[2995]);
            out[1467] = temp;
        }
        if (history[2996] == 0){
            out[1468] = NAN;
        } else {
            temp = ((history[2997] == -INFINITY) ? NAN : history[2997]);
            out[1468] = temp;
        }
        if (history[2998] == 0){
            out[1469] = NAN;
        } else {
            out[1469] = history[2999]/history[2998];
        }
        if (history[3000] == 0){
            out[1470] = NAN;
        } else {
            temp_mean = history[3001]/history[3000];
            out[1470] = sqrt((
                history[3002] - pow(temp_mean, 2) * history[3000]
            )/(history[3000]-1));
        }
        if (history[3003] == 0){
            out[1471] = NAN;
        } else {
            temp_mean = history[3004]/history[3003];
            out[1471] = sqrt((
                history[3005] - pow(temp_mean, 2) * history[3003]
            )/(history[3003]-1));
        }
        if (history[3006] == 0){
            out[1472] = NAN;
        } else {
            temp_mean = history[3007]/history[3006];
            out[1472] = sqrt((
                history[3008] - pow(temp_mean, 2) * history[3006]
            )/(history[3006]-1));
        }
        if (history[3009] == 0){
            out[1473] = NAN;
        } else {
            temp_mean = history[3010]/history[3009];
            out[1473] = sqrt((
                history[3011] - pow(temp_mean, 2) * history[3009]
            )/(history[3009]-1));
        }
        if (history[3012] == 0){
            out[1474] = NAN;
        } else {
            temp = ((history[3013] == -INFINITY) ? NAN : history[3013]);
            out[1474] = temp;
        }
        if (history[3014] == 0){
            out[1475] = NAN;
        } else {
            out[1475] = history[3015];
        }
            out[1476] = history[3084] - history[1562];
            out[1477] = history[3072] - history[1572];
            out[1478] = history[3082] - history[1507];
            out[1479] = history[2985] - history[1533];
            out[1480] = history[2959] - history[1512];
            out[1481] = history[2987] - history[1607];
            out[1482] = history[2975] - history[1494];
            out[1483] = history[2965] - history[1565];
            out[1484] = history[3076] - history[1523];
            out[1485] = history[3060] - history[1534];
            out[1486] = history[2969] - history[1599];
        if (history[3016] == 0){
            out[1487] = NAN;
        } else {
            temp = ((history[3017] == -INFINITY) ? NAN : history[3017]);
            out[1487] = temp;
        }
        if (history[3018] == 0){
            out[1488] = NAN;
        } else {
            temp_mean = history[3019]/history[3018];
            out[1488] = sqrt((
                history[3020] - pow(temp_mean, 2) * history[3018]
            )/(history[3018]-1));
        }
        if (history[3021] == 0){
            out[1489] = NAN;
        } else {
            temp_mean = history[3022]/history[3021];
            out[1489] = sqrt((
                history[3023] - pow(temp_mean, 2) * history[3021]
            )/(history[3021]-1));
        }
        if (history[3024] == 0){
            out[1490] = NAN;
        } else {
            temp_mean = history[3025]/history[3024];
            out[1490] = sqrt((
                history[3026] - pow(temp_mean, 2) * history[3024]
            )/(history[3024]-1));
        }
        if (history[3027] == 0){
            out[1491] = NAN;
        } else {
            out[1491] = history[3028];
        }
        if (history[3029] == 0){
            out[1492] = NAN;
        } else {
            out[1492] = history[3030];
        }
        if (history[3031] == 0){
            out[1493] = NAN;
        } else {
            temp = ((history[3032] == -INFINITY) ? NAN : history[3032]);
            out[1493] = temp;
        }
        if (history[3033] == 0){
            out[1494] = NAN;
        } else {
            temp_mean = history[3034]/history[3033];
            out[1494] = sqrt((
                history[3035] - pow(temp_mean, 2) * history[3033]
            )/(history[3033]-1));
        }
        if (history[3036] == 0){
            out[1495] = NAN;
        } else {
            out[1495] = history[3037];
        }
        if (history[3038] == 0){
            out[1496] = NAN;
        } else {
            out[1496] = history[3039]/history[3038];
        }
        if (history[3040] == 0){
            out[1497] = NAN;
        } else {
            temp_mean = history[3041]/history[3040];
            out[1497] = sqrt((
                history[3042] - pow(temp_mean, 2) * history[3040]
            )/(history[3040]-1));
        }
        if (history[3043] == 0){
            out[1498] = NAN;
        } else {
            temp_mean = history[3044]/history[3043];
            out[1498] = sqrt((
                history[3045] - pow(temp_mean, 2) * history[3043]
            )/(history[3043]-1));
        }
        if (history[3046] == 0){
            out[1499] = NAN;
        } else {
            out[1499] = history[3047]/history[3046];
        }
        if (history[3048] == 0){
            out[1500] = NAN;
        } else {
            out[1500] = ((history[3049] == INFINITY) ? NAN : history[3049]);
        }
        if (history[3050] == 0){
            out[1501] = NAN;
        } else {
            out[1501] = history[3051]/history[3050];
        }
        if (history[3052] == 0){
            out[1502] = NAN;
        } else {
            out[1502] = history[3053]/history[3052];
        }
        if (history[3054] == 0){
            out[1503] = NAN;
        } else {
            out[1503] = ((history[3055] == INFINITY) ? NAN : history[3055]);
        }
        if (history[3056] == 0){
            out[1504] = NAN;
        } else {
            temp_mean = history[3057]/history[3056];
            out[1504] = sqrt((
                history[3058] - pow(temp_mean, 2) * history[3056]
            )/(history[3056]-1));
        }
            out[1505] = history[3068] - history[1510];
            out[1506] = history[3062] - history[1552];
            out[1507] = history[2977] - history[1552];
            out[1508] = history[2961] - history[1536];
            out[1509] = history[2971] - history[1515];
            out[1510] = history[3070] - history[1612];
            out[1511] = history[2967] - history[1612];
            out[1512] = history[2983] - history[1612];
            out[1513] = history[3088] - history[1612];
            out[1514] = history[3090] - history[1604];
            out[1515] = history[3074] - history[1587];
            out[1516] = history[2973] - history[1591];
            out[1517] = history[3078] - history[1595];
            out[1518] = history[2981] - history[1585];
            out[1519] = history[3080] - history[1585];
            out[1520] = history[3086] - history[1497];
            out[1521] = history[2963] - history[1488];
            out[1522] = history[2979] - history[1525];
            out[1523] = history[3064] - history[1525];
            out[1524] = history[3066] - history[1605];
        if (history[1615] == 0){
            out[1525] = NAN;
        } else {
            temp = ((history[1616] == -INFINITY) ? NAN : history[1616]);
            out[1525] = temp;
        }
        if (history[3105] == 0){
            out[1526] = NAN;
        } else {
            temp = ((history[3106] == -INFINITY) ? NAN : history[3106]);
            out[1526] = temp;
        }
        if (history[3107] == 0){
            out[1527] = NAN;
        } else {
            out[1527] = history[3108]/history[3107];
        }
        if (history[3109] == 0){
            out[1528] = NAN;
        } else {
            out[1528] = history[3110]/history[3109];
        }
        if (history[3111] == 0){
            out[1529] = NAN;
        } else {
            out[1529] = history[3112];
        }
        if (history[3113] == 0){
            out[1530] = NAN;
        } else {
            temp = ((history[3114] == -INFINITY) ? NAN : history[3114]);
            out[1530] = temp;
        }
        if (history[3115] == 0){
            out[1531] = NAN;
        } else {
            out[1531] = history[3116]/history[3115];
        }
        if (history[3117] == 0){
            out[1532] = NAN;
        } else {
            out[1532] = ((history[3118] == INFINITY) ? NAN : history[3118]);
        }
        if (history[3119] == 0){
            out[1533] = NAN;
        } else {
            out[1533] = history[3120];
        }
        if (history[3121] == 0){
            out[1534] = NAN;
        } else {
            temp = ((history[3122] == -INFINITY) ? NAN : history[3122]);
            out[1534] = temp;
        }
        if (history[3123] == 0){
            out[1535] = NAN;
        } else {
            temp = ((history[3124] == -INFINITY) ? NAN : history[3124]);
            out[1535] = temp;
        }
        if (history[3125] == 0){
            out[1536] = NAN;
        } else {
            temp_mean = history[3126]/history[3125];
            out[1536] = sqrt((
                history[3127] - pow(temp_mean, 2) * history[3125]
            )/(history[3125]-1));
        }
        if (history[3128] == 0){
            out[1537] = NAN;
        } else {
            out[1537] = history[3129]/history[3128];
        }
        if (history[3130] == 0){
            out[1538] = NAN;
        } else {
            out[1538] = history[3131];
        }
        if (history[3132] == 0){
            out[1539] = NAN;
        } else {
            out[1539] = history[3133]/history[3132];
        }
        if (history[3134] == 0){
            out[1540] = NAN;
        } else {
            temp_mean = history[3135]/history[3134];
            out[1540] = sqrt((
                history[3136] - pow(temp_mean, 2) * history[3134]
            )/(history[3134]-1));
        }
            out[1541] = history[3098] - history[1627];
            out[1542] = history[3100] - history[1673];
            out[1543] = history[3092] - history[1669];
            out[1544] = history[3096] - history[1669];
            out[1545] = history[3138] - history[1648];
            out[1546] = history[3102] - history[1652];
            out[1547] = history[3140] - history[1629];
            out[1548] = history[3104] - history[1623];
            out[1549] = history[3094] - history[1623];
            out[1550] = history[3142] - history[1625];
        out[1551] = history[1683];
        out[1552] = history[1672];
    }
    if (lg >= 2){
        if (history[1688] == 0){
            out[1553] = NAN;
        } else {
            out[1553] = history[1689];
        }
        if (history[1690] == 0){
            out[1554] = NAN;
        } else {
            temp = ((history[1691] == -INFINITY) ? NAN : history[1691]);
            out[1554] = temp;
        }
        if (history[1690] == 0){
            out[1555] = NAN;
        } else {
            out[1555] = history[1692];
        }
        if (history[1693] == 0){
            out[1556] = NAN;
        } else {
            out[1556] = ((history[1694] == INFINITY) ? NAN : history[1694]);
        }
        out[1557] = history[1695];
        if (history[1696] == 0){
            out[1558] = NAN;
        } else {
            out[1558] = ((history[1697] == INFINITY) ? NAN : history[1697]);
        }
        if (history[1698] == 0){
            out[1559] = NAN;
        } else {
            out[1559] = ((history[1699] == INFINITY) ? NAN : history[1699]);
        }
        if (history[1700] == 0){
            out[1560] = NAN;
        } else {
            temp = ((history[1701] == -INFINITY) ? NAN : history[1701]);
            out[1560] = temp;
        }
        if (history[1702] == 0){
            out[1561] = NAN;
        } else {
            out[1561] = ((history[1703] == INFINITY) ? NAN : history[1703]);
        }
        if (history[1702] == 0){
            out[1562] = NAN;
        } else {
            temp = ((history[1704] == -INFINITY) ? NAN : history[1704]);
            out[1562] = temp;
        }
        if (history[1702] == 0){
            out[1563] = NAN;
        } else {
            out[1563] = history[1705];
        }
        if (history[1702] == 0){
            out[1564] = NAN;
        } else {
            out[1564] = history[1705]/history[1702];
        }
        if (history[1706] == 0){
            out[1565] = NAN;
        } else {
            temp_mean = history[1707]/history[1706];
            out[1565] = sqrt((
                history[1708] - pow(temp_mean, 2) * history[1706]
            )/(history[1706]-1));
        }
        if (history[1709] == 0){
            out[1566] = NAN;
        } else {
            temp_mean = history[1710]/history[1709];
            out[1566] = sqrt((
                history[1711] - pow(temp_mean, 2) * history[1709]
            )/(history[1709]-1));
        }
        if (history[1712] == 0){
            out[1567] = NAN;
        } else {
            out[1567] = history[1713];
        }
        if (history[1714] == 0){
            out[1568] = NAN;
        } else {
            out[1568] = history[1715]/history[1714];
        }
        if (history[3143] == 0){
            out[1569] = NAN;
        } else {
            out[1569] = history[3144]/history[3143];
        }
        if (history[1720] == 0){
            out[1570] = NAN;
        } else {
            temp = ((history[1721] == -INFINITY) ? NAN : history[1721]);
            out[1570] = temp;
        }
        if (history[3145] == 0){
            out[1571] = NAN;
        } else {
            out[1571] = history[3146];
        }
            out[1572] = history[3148] - history[1725];
        if (history[3149] == 0){
            out[1573] = NAN;
        } else {
            out[1573] = history[3150]/history[3149];
        }
        if (history[3151] == 0){
            out[1574] = NAN;
        } else {
            out[1574] = history[3152];
        }
        if (history[3153] == 0){
            out[1575] = NAN;
        } else {
            out[1575] = history[3154];
        }
            out[1576] = history[3156] - history[1743];
        if (history[3157] == 0){
            out[1577] = NAN;
        } else {
            temp = ((history[3158] == -INFINITY) ? NAN : history[3158]);
            out[1577] = temp;
        }
        if (history[3159] == 0){
            out[1578] = NAN;
        } else {
            out[1578] = history[3160];
        }
            out[1579] = history[3162] - history[1753];
        if (history[3165] == 0){
            out[1580] = NAN;
        } else {
            temp = ((history[3166] == -INFINITY) ? NAN : history[3166]);
            out[1580] = temp;
        }
            out[1581] = history[3168] - history[1765];
            out[1582] = history[3164] - history[1765];
            out[1583] = history[3170] - history[1761];
        if (history[3171] == 0){
            out[1584] = NAN;
        } else {
            out[1584] = history[3172]/history[3171];
        }
        if (history[3173] == 0){
            out[1585] = NAN;
        } else {
            out[1585] = history[3174]/history[3173];
        }
        if (history[3175] == 0){
            out[1586] = NAN;
        } else {
            out[1586] = ((history[3176] == INFINITY) ? NAN : history[3176]);
        }
        if (history[3177] == 0){
            out[1587] = NAN;
        } else {
            out[1587] = ((history[3178] == INFINITY) ? NAN : history[3178]);
        }
            out[1588] = history[3180] - history[1783];
        if (history[3181] == 0){
            out[1589] = NAN;
        } else {
            out[1589] = history[3182];
        }
    }
}

    
void add_features_batch(int lg, float* out, double* history, int num_rows){

    for (int i = 0; i < num_rows; i++){ // num_rows => 3
        // out + index => use array + index to get the pointer to the index’th item of an array.
        add_features(lg, out + (1590 * i), history); // out + (1590 * i) => out + 0, out + 1590, out + 3180
    }
}