# Generated from d:\Study\Year_3\PPL_2\BTL_10\assignment3\initial\src\main\csel\parser\CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0099\n\2\f\2\16\2\u009c\13\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u00a3\n\3\f\3\16\3\u00a6\13\3\3\4\6\4\u00a9\n")
        buf.write("\4\r\4\16\4\u00aa\3\5\6\5\u00ae\n\5\r\5\16\5\u00af\3\5")
        buf.write("\5\5\u00b3\n\5\3\5\3\5\3\5\5\5\u00b8\n\5\5\5\u00ba\n\5")
        buf.write("\3\6\3\6\5\6\u00be\n\6\3\7\3\7\7\7\u00c2\n\7\f\7\16\7")
        buf.write("\u00c5\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\68\u0184\n8\r8\168\u0185")
        buf.write("\38\38\39\39\39\39\79\u018e\n9\f9\169\u0191\139\39\39")
        buf.write("\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\7A\u01a8\nA\fA\16A\u01ab\13A\3B\3B\5B\u01af\nB\3")
        buf.write("B\6B\u01b2\nB\rB\16B\u01b3\3C\3C\3C\3C\5C\u01ba\nC\3D")
        buf.write("\3D\3D\3E\3E\3E\3E\5E\u01c3\nE\3F\3F\7F\u01c7\nF\fF\16")
        buf.write("F\u01ca\13F\3F\5F\u01cd\nF\3F\3F\3G\3G\7G\u01d3\nG\fG")
        buf.write("\16G\u01d6\13G\3G\3G\3G\3H\3H\3H\3H\7H\u01df\nH\fH\16")
        buf.write("H\u01e2\13H\3H\3H\3I\3I\3I\4\u018f\u01e0\2J\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\2-\2/\27\61\30\63\31")
        buf.write("\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W")
        buf.write("+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s\2u\2w\2y")
        buf.write("\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2")
        buf.write("\u008b9\u008d:\u008f;\u0091<\3\2\f\5\2\13\f\17\17\"\"")
        buf.write("\3\2\62;\3\2C\\\3\2c|\4\2GGgg\4\2--//\7\2\f\f\17\17$$")
        buf.write("))^^\t\2))^^ddhhppttvv\3\2$$\4\3\f\f\17\17\2\u01f3\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2")
        buf.write("\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093")
        buf.write("\3\2\2\2\5\u009d\3\2\2\2\7\u00a8\3\2\2\2\t\u00ad\3\2\2")
        buf.write("\2\13\u00bd\3\2\2\2\r\u00bf\3\2\2\2\17\u00c9\3\2\2\2\21")
        buf.write("\u00cf\3\2\2\2\23\u00d8\3\2\2\2\25\u00dd\3\2\2\2\27\u00e2")
        buf.write("\3\2\2\2\31\u00e6\3\2\2\2\33\u00ef\3\2\2\2\35\u00f2\3")
        buf.write("\2\2\2\37\u00f9\3\2\2\2!\u0100\3\2\2\2#\u0106\3\2\2\2")
        buf.write("%\u010b\3\2\2\2\'\u010e\3\2\2\2)\u0111\3\2\2\2+\u0115")
        buf.write("\3\2\2\2-\u011a\3\2\2\2/\u0120\3\2\2\2\61\u0128\3\2\2")
        buf.write("\2\63\u012f\3\2\2\2\65\u0134\3\2\2\2\67\u013a\3\2\2\2")
        buf.write("9\u0143\3\2\2\2;\u0145\3\2\2\2=\u0147\3\2\2\2?\u0149\3")
        buf.write("\2\2\2A\u014b\3\2\2\2C\u014d\3\2\2\2E\u014f\3\2\2\2G\u0152")
        buf.write("\3\2\2\2I\u0155\3\2\2\2K\u0158\3\2\2\2M\u015b\3\2\2\2")
        buf.write("O\u015d\3\2\2\2Q\u015f\3\2\2\2S\u0162\3\2\2\2U\u0165\3")
        buf.write("\2\2\2W\u0167\3\2\2\2Y\u016b\3\2\2\2[\u016e\3\2\2\2]\u0170")
        buf.write("\3\2\2\2_\u0172\3\2\2\2a\u0174\3\2\2\2c\u0176\3\2\2\2")
        buf.write("e\u0178\3\2\2\2g\u017a\3\2\2\2i\u017c\3\2\2\2k\u017e\3")
        buf.write("\2\2\2m\u0180\3\2\2\2o\u0183\3\2\2\2q\u0189\3\2\2\2s\u0197")
        buf.write("\3\2\2\2u\u0199\3\2\2\2w\u019b\3\2\2\2y\u019d\3\2\2\2")
        buf.write("{\u019f\3\2\2\2}\u01a1\3\2\2\2\177\u01a3\3\2\2\2\u0081")
        buf.write("\u01a5\3\2\2\2\u0083\u01ac\3\2\2\2\u0085\u01b9\3\2\2\2")
        buf.write("\u0087\u01bb\3\2\2\2\u0089\u01c2\3\2\2\2\u008b\u01c4\3")
        buf.write("\2\2\2\u008d\u01d0\3\2\2\2\u008f\u01da\3\2\2\2\u0091\u01e5")
        buf.write("\3\2\2\2\u0093\u009a\5{>\2\u0094\u0099\5w<\2\u0095\u0099")
        buf.write("\5u;\2\u0096\u0099\5s:\2\u0097\u0099\5y=\2\u0098\u0094")
        buf.write("\3\2\2\2\u0098\u0095\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\4\3\2\2\2\u009c\u009a\3\2\2")
        buf.write("\2\u009d\u00a4\5w<\2\u009e\u00a3\5w<\2\u009f\u00a3\5u")
        buf.write(";\2\u00a0\u00a3\5s:\2\u00a1\u00a3\5y=\2\u00a2\u009e\3")
        buf.write("\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\6\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7")
        buf.write("\u00a9\5s:\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\b\3\2\2\2\u00ac")
        buf.write("\u00ae\5s:\2\u00ad\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b9\3\2\2\2")
        buf.write("\u00b1\u00b3\5\u0081A\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00ba\5\u0083B\2\u00b5")
        buf.write("\u00b7\5\u0081A\2\u00b6\u00b8\5\u0083B\2\u00b7\u00b6\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b2")
        buf.write("\3\2\2\2\u00b9\u00b5\3\2\2\2\u00ba\n\3\2\2\2\u00bb\u00be")
        buf.write("\5+\26\2\u00bc\u00be\5-\27\2\u00bd\u00bb\3\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\f\3\2\2\2\u00bf\u00c3\7$\2\2\u00c0")
        buf.write("\u00c2\5\u0085C\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2")
        buf.write("\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\7$\2\2\u00c7")
        buf.write("\u00c8\b\7\2\2\u00c8\16\3\2\2\2\u00c9\u00ca\7D\2\2\u00ca")
        buf.write("\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7c\2\2\u00cd")
        buf.write("\u00ce\7m\2\2\u00ce\20\3\2\2\2\u00cf\u00d0\7E\2\2\u00d0")
        buf.write("\u00d1\7q\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7w\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\22\3\2\2\2\u00d8\u00d9\7G\2\2\u00d9")
        buf.write("\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc")
        buf.write("\24\3\2\2\2\u00dd\u00de\7G\2\2\u00de\u00df\7n\2\2\u00df")
        buf.write("\u00e0\7k\2\2\u00e0\u00e1\7h\2\2\u00e1\26\3\2\2\2\u00e2")
        buf.write("\u00e3\7H\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("\30\3\2\2\2\u00e6\u00e7\7H\2\2\u00e7\u00e8\7w\2\2\u00e8")
        buf.write("\u00e9\7p\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb\7v\2\2\u00eb")
        buf.write("\u00ec\7k\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\32\3\2\2\2\u00ef\u00f0\7K\2\2\u00f0\u00f1\7h\2\2\u00f1")
        buf.write("\34\3\2\2\2\u00f2\u00f3\7T\2\2\u00f3\u00f4\7g\2\2\u00f4")
        buf.write("\u00f5\7v\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7t\2\2\u00f7")
        buf.write("\u00f8\7p\2\2\u00f8\36\3\2\2\2\u00f9\u00fa\7P\2\2\u00fa")
        buf.write("\u00fb\7w\2\2\u00fb\u00fc\7o\2\2\u00fc\u00fd\7d\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe\u00ff\7t\2\2\u00ff \3\2\2\2\u0100")
        buf.write("\u0101\7Y\2\2\u0101\u0102\7j\2\2\u0102\u0103\7k\2\2\u0103")
        buf.write("\u0104\7n\2\2\u0104\u0105\7g\2\2\u0105\"\3\2\2\2\u0106")
        buf.write("\u0107\7E\2\2\u0107\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109")
        buf.write("\u010a\7n\2\2\u010a$\3\2\2\2\u010b\u010c\7Q\2\2\u010c")
        buf.write("\u010d\7h\2\2\u010d&\3\2\2\2\u010e\u010f\7K\2\2\u010f")
        buf.write("\u0110\7p\2\2\u0110(\3\2\2\2\u0111\u0112\7N\2\2\u0112")
        buf.write("\u0113\7g\2\2\u0113\u0114\7v\2\2\u0114*\3\2\2\2\u0115")
        buf.write("\u0116\7V\2\2\u0116\u0117\7t\2\2\u0117\u0118\7w\2\2\u0118")
        buf.write("\u0119\7g\2\2\u0119,\3\2\2\2\u011a\u011b\7H\2\2\u011b")
        buf.write("\u011c\7c\2\2\u011c\u011d\7n\2\2\u011d\u011e\7u\2\2\u011e")
        buf.write("\u011f\7g\2\2\u011f.\3\2\2\2\u0120\u0121\7D\2\2\u0121")
        buf.write("\u0122\7q\2\2\u0122\u0123\7q\2\2\u0123\u0124\7n\2\2\u0124")
        buf.write("\u0125\7g\2\2\u0125\u0126\7c\2\2\u0126\u0127\7p\2\2\u0127")
        buf.write("\60\3\2\2\2\u0128\u0129\7U\2\2\u0129\u012a\7v\2\2\u012a")
        buf.write("\u012b\7t\2\2\u012b\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d")
        buf.write("\u012e\7i\2\2\u012e\62\3\2\2\2\u012f\u0130\7L\2\2\u0130")
        buf.write("\u0131\7U\2\2\u0131\u0132\7Q\2\2\u0132\u0133\7P\2\2\u0133")
        buf.write("\64\3\2\2\2\u0134\u0135\7C\2\2\u0135\u0136\7t\2\2\u0136")
        buf.write("\u0137\7t\2\2\u0137\u0138\7c\2\2\u0138\u0139\7{\2\2\u0139")
        buf.write("\66\3\2\2\2\u013a\u013b\7E\2\2\u013b\u013c\7q\2\2\u013c")
        buf.write("\u013d\7p\2\2\u013d\u013e\7u\2\2\u013e\u013f\7v\2\2\u013f")
        buf.write("\u0140\7c\2\2\u0140\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142")
        buf.write("8\3\2\2\2\u0143\u0144\7-\2\2\u0144:\3\2\2\2\u0145\u0146")
        buf.write("\7/\2\2\u0146<\3\2\2\2\u0147\u0148\7,\2\2\u0148>\3\2\2")
        buf.write("\2\u0149\u014a\7\61\2\2\u014a@\3\2\2\2\u014b\u014c\7\'")
        buf.write("\2\2\u014cB\3\2\2\2\u014d\u014e\7#\2\2\u014eD\3\2\2\2")
        buf.write("\u014f\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151F\3\2\2\2")
        buf.write("\u0152\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154H\3\2\2\2")
        buf.write("\u0155\u0156\7?\2\2\u0156\u0157\7?\2\2\u0157J\3\2\2\2")
        buf.write("\u0158\u0159\7#\2\2\u0159\u015a\7?\2\2\u015aL\3\2\2\2")
        buf.write("\u015b\u015c\7>\2\2\u015cN\3\2\2\2\u015d\u015e\7@\2\2")
        buf.write("\u015eP\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7?\2\2")
        buf.write("\u0161R\3\2\2\2\u0162\u0163\7@\2\2\u0163\u0164\7?\2\2")
        buf.write("\u0164T\3\2\2\2\u0165\u0166\7?\2\2\u0166V\3\2\2\2\u0167")
        buf.write("\u0168\7?\2\2\u0168\u0169\7?\2\2\u0169\u016a\7\60\2\2")
        buf.write("\u016aX\3\2\2\2\u016b\u016c\7-\2\2\u016c\u016d\7\60\2")
        buf.write("\2\u016dZ\3\2\2\2\u016e\u016f\7*\2\2\u016f\\\3\2\2\2\u0170")
        buf.write("\u0171\7+\2\2\u0171^\3\2\2\2\u0172\u0173\7]\2\2\u0173")
        buf.write("`\3\2\2\2\u0174\u0175\7_\2\2\u0175b\3\2\2\2\u0176\u0177")
        buf.write("\7<\2\2\u0177d\3\2\2\2\u0178\u0179\7\60\2\2\u0179f\3\2")
        buf.write("\2\2\u017a\u017b\7.\2\2\u017bh\3\2\2\2\u017c\u017d\7=")
        buf.write("\2\2\u017dj\3\2\2\2\u017e\u017f\7}\2\2\u017fl\3\2\2\2")
        buf.write("\u0180\u0181\7\177\2\2\u0181n\3\2\2\2\u0182\u0184\t\2")
        buf.write("\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write("\u0188\b8\3\2\u0188p\3\2\2\2\u0189\u018a\7%\2\2\u018a")
        buf.write("\u018b\7%\2\2\u018b\u018f\3\2\2\2\u018c\u018e\13\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0193\7%\2\2\u0193\u0194\7%\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\b9\3\2\u0196r\3\2\2\2\u0197\u0198")
        buf.write("\t\3\2\2\u0198t\3\2\2\2\u0199\u019a\t\4\2\2\u019av\3\2")
        buf.write("\2\2\u019b\u019c\t\5\2\2\u019cx\3\2\2\2\u019d\u019e\7")
        buf.write("a\2\2\u019ez\3\2\2\2\u019f\u01a0\7&\2\2\u01a0|\3\2\2\2")
        buf.write("\u01a1\u01a2\t\6\2\2\u01a2~\3\2\2\2\u01a3\u01a4\t\7\2")
        buf.write("\2\u01a4\u0080\3\2\2\2\u01a5\u01a9\5e\63\2\u01a6\u01a8")
        buf.write("\5s:\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u0082\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u01ae\5}?\2\u01ad\u01af\5\177@\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3")
        buf.write("\2\2\2\u01b0\u01b2\5s:\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u0084\3\2\2\2\u01b5\u01ba\n\b\2\2\u01b6\u01ba\5\u0087")
        buf.write("D\2\u01b7\u01b8\7)\2\2\u01b8\u01ba\7$\2\2\u01b9\u01b5")
        buf.write("\3\2\2\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u0086\3\2\2\2\u01bb\u01bc\7^\2\2\u01bc\u01bd\t\t\2\2")
        buf.write("\u01bd\u0088\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c3\n")
        buf.write("\t\2\2\u01c0\u01c1\7)\2\2\u01c1\u01c3\n\n\2\2\u01c2\u01be")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u008a\3\2\2\2\u01c4")
        buf.write("\u01c8\7$\2\2\u01c5\u01c7\5\u0085C\2\u01c6\u01c5\3\2\2")
        buf.write("\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01cd\t\13\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2")
        buf.write("\2\u01ce\u01cf\bF\4\2\u01cf\u008c\3\2\2\2\u01d0\u01d4")
        buf.write("\7$\2\2\u01d1\u01d3\5\u0085C\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\5")
        buf.write("\u0089E\2\u01d8\u01d9\bG\5\2\u01d9\u008e\3\2\2\2\u01da")
        buf.write("\u01db\7%\2\2\u01db\u01dc\7%\2\2\u01dc\u01e0\3\2\2\2\u01dd")
        buf.write("\u01df\13\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2")
        buf.write("\2\u01e0\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e3")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\bH\6\2\u01e4")
        buf.write("\u0090\3\2\2\2\u01e5\u01e6\13\2\2\2\u01e6\u01e7\bI\7\2")
        buf.write("\u01e7\u0092\3\2\2\2\31\2\u0098\u009a\u00a2\u00a4\u00aa")
        buf.write("\u00af\u00b2\u00b7\u00b9\u00bd\u00c3\u0185\u018f\u01a9")
        buf.write("\u01ae\u01b3\u01b9\u01c2\u01c8\u01cc\u01d4\u01e0\b\3\7")
        buf.write("\2\b\2\2\3F\3\3G\4\3H\5\3I\6")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDD = 1
    IDND = 2
    INT = 3
    FLOAT = 4
    BOOLEAN_LIT = 5
    STRING_LIT = 6
    BREAK = 7
    CONTINUE = 8
    ELSE = 9
    ELIF = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    RETURN = 14
    NUMBER = 15
    WHILE = 16
    CALL = 17
    OF = 18
    IN = 19
    LET = 20
    BOOLEAN = 21
    STRING = 22
    JSON = 23
    ARRAY = 24
    CONSTANT = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    FACT = 31
    AND = 32
    OR = 33
    EQU = 34
    NQU = 35
    LT = 36
    GT = 37
    LTE = 38
    GTE = 39
    EQUAL = 40
    EQUDOT = 41
    ADDDOT = 42
    LP = 43
    RP = 44
    LSB = 45
    RSB = 46
    COLON = 47
    DOT = 48
    COMMA = 49
    SEMI = 50
    LCB = 51
    RCB = 52
    WS = 53
    COMMENT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    UNTERMINATED_COMMENT = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'Else'", "'Elif'", "'For'", "'Function'", 
            "'If'", "'Return'", "'Number'", "'While'", "'Call'", "'Of'", 
            "'In'", "'Let'", "'Boolean'", "'String'", "'JSON'", "'Array'", 
            "'Constant'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "'==.'", "'+.'", "'('", "')'", "'['", "']'", "':'", "'.'", "','", 
            "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IDD", "IDND", "INT", "FLOAT", "BOOLEAN_LIT", "STRING_LIT", 
            "BREAK", "CONTINUE", "ELSE", "ELIF", "FOR", "FUNCTION", "IF", 
            "RETURN", "NUMBER", "WHILE", "CALL", "OF", "IN", "LET", "BOOLEAN", 
            "STRING", "JSON", "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "FACT", "AND", "OR", "EQU", "NQU", "LT", "GT", 
            "LTE", "GTE", "EQUAL", "EQUDOT", "ADDDOT", "LP", "RP", "LSB", 
            "RSB", "COLON", "DOT", "COMMA", "SEMI", "LCB", "RCB", "WS", 
            "COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "IDD", "IDND", "INT", "FLOAT", "BOOLEAN_LIT", "STRING_LIT", 
                  "BREAK", "CONTINUE", "ELSE", "ELIF", "FOR", "FUNCTION", 
                  "IF", "RETURN", "NUMBER", "WHILE", "CALL", "OF", "IN", 
                  "LET", "TRUE", "FALSE", "BOOLEAN", "STRING", "JSON", "ARRAY", 
                  "CONSTANT", "ADD", "SUB", "MUL", "DIV", "MOD", "FACT", 
                  "AND", "OR", "EQU", "NQU", "LT", "GT", "LTE", "GTE", "EQUAL", 
                  "EQUDOT", "ADDDOT", "LP", "RP", "LSB", "RSB", "COLON", 
                  "DOT", "COMMA", "SEMI", "LCB", "RCB", "WS", "COMMENT", 
                  "DIGIT", "UPPER_CHAR", "LOWER_CHAR", "DASH", "DOLLAR", 
                  "E", "SIGN", "DECIMAL_PART", "EXPONENT_PART", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.STRING_LIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNTERMINATED_COMMENT_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		s = str(self.text)
            		self.text = s[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		s = str(self.text)
            		if s[-1] in ['\n', '\r']:
            			raise UncloseString(s[1:-1])
            		else:
            			raise UncloseString(s[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		s = str(self.text)
            		raise IllegalEscape(s[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UnterminatedComment()
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		raise ErrorToken(self.text)
            	
     


