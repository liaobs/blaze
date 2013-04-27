
# D:\Develop\blaze-core\blaze\datashape\dyacc.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x99h\xb7\xcd\xe4\x05\xc3\x8d\xe5\xab2?\x11\x00\xeb\xd1'
    
_lr_action_items = {'LBRACE':([0,1,2,3,5,6,7,8,10,12,13,14,22,25,27,35,36,38,40,42,43,44,46,48,],[9,-5,-12,-13,-3,-11,-10,-9,-8,9,9,9,9,9,9,9,-25,-14,9,-23,9,-24,9,-4,]),'NAME':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,22,23,24,25,27,35,36,37,38,39,40,42,43,44,46,48,],[2,-5,-12,-13,-3,-11,-10,-9,21,-8,24,2,26,26,2,24,-7,2,2,2,-25,21,-14,24,2,-23,26,-24,2,-4,]),'SEMI':([2,3,6,7,8,9,10,16,17,20,36,37,38,42,44,45,47,52,],[-12,-13,-11,-10,-9,-34,-8,37,-27,-28,-25,-34,-14,-23,-24,-33,37,-32,]),')':([2,3,6,7,8,10,26,28,29,30,31,32,33,34,36,38,41,42,44,49,50,51,],[-12,-13,-11,-10,-9,-8,-18,-20,-16,-15,42,-19,-21,44,-25,-14,49,-23,-24,-17,-22,52,]),'(':([2,6,13,14,26,32,35,43,],[13,14,27,27,13,14,46,27,]),'NUMBER':([0,1,2,3,5,6,7,8,10,12,13,14,22,25,27,35,36,38,40,42,43,44,46,48,],[3,-5,-12,-13,-3,-11,-10,-9,-8,3,28,28,3,3,3,3,-25,-14,3,-23,28,-24,3,-4,]),'RBRACE':([2,3,6,7,8,9,10,16,17,20,36,37,38,42,44,45,47,52,],[-12,-13,-11,-10,-9,-34,-8,36,-27,-28,-25,-34,-14,-23,-24,-33,-26,-32,]),'EQUALS':([23,24,39,],[40,-7,-6,]),'STRING':([13,14,43,],[33,33,33,]),'COMMA':([2,3,6,7,8,10,26,28,29,30,31,32,33,34,36,38,42,44,49,50,],[-12,-13,-11,-10,-9,22,-18,-20,-16,-15,43,-19,-21,43,-25,22,-23,-24,-17,43,]),'COLON':([15,18,19,21,],[35,-30,-31,-29,]),'BIT':([0,1,2,3,5,6,7,8,9,10,12,13,14,22,25,27,35,36,37,38,40,42,43,44,46,48,],[6,-5,-12,-13,-3,-11,-10,-9,18,-8,6,32,32,6,6,6,6,-25,18,-14,6,-23,32,-24,6,-4,]),'TYPE':([0,1,2,3,5,6,7,8,9,10,12,25,36,37,38,42,44,48,],[11,-5,-12,-13,-3,-11,-10,-9,19,-8,11,11,-25,19,-14,-23,-24,-4,]),'$end':([1,2,3,4,5,6,7,8,10,12,25,36,38,42,44,48,],[-5,-12,-13,0,-3,-11,-10,-9,-8,-1,-2,-25,-14,-23,-24,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rhs_expression':([0,12,25,27,35,40,46,],[1,1,1,41,45,48,51,]),'record_opt':([9,37,],[16,47,]),'top':([0,],[4,]),'stmt':([0,12,25,],[5,5,5,]),'record':([0,12,13,14,22,25,27,35,40,43,46,],[7,7,29,29,7,7,7,7,7,29,7,]),'appl':([0,12,13,14,22,25,27,35,40,43,46,],[8,8,30,30,8,8,8,8,8,30,8,]),'record_item':([9,37,],[17,17,]),'appl_args':([13,14,43,],[31,34,50,]),'record_name':([9,37,],[15,15,]),'rhs_expression_list':([0,12,22,25,27,35,40,46,],[10,10,38,10,10,10,10,10,]),'lhs_expression':([11,23,39,],[23,39,39,]),'empty':([9,37,],[20,20,]),'mod':([0,12,25,],[12,25,25,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> top","S'",1,None,None,None),
  ('top -> mod','top',1,'p_top','',173),
  ('mod -> mod mod','mod',2,'p_decl1','',180),
  ('mod -> stmt','mod',1,'p_decl2','',184),
  ('stmt -> TYPE lhs_expression EQUALS rhs_expression','stmt',4,'p_statement_assign','',190),
  ('stmt -> rhs_expression','stmt',1,'p_statement_expr','',208),
  ('lhs_expression -> lhs_expression lhs_expression','lhs_expression',2,'p_lhs_expression','',214),
  ('lhs_expression -> NAME','lhs_expression',1,'p_lhs_expression_node','',219),
  ('rhs_expression -> rhs_expression_list','rhs_expression',1,'p_rhs_expression','',225),
  ('rhs_expression_list -> appl','rhs_expression_list',1,'p_rhs_expression_list_node1','',232),
  ('rhs_expression_list -> record','rhs_expression_list',1,'p_rhs_expression_list_node1','',233),
  ('rhs_expression_list -> BIT','rhs_expression_list',1,'p_rhs_expression_list__bit','',237),
  ('rhs_expression_list -> NAME','rhs_expression_list',1,'p_rhs_expression_list__name','',241),
  ('rhs_expression_list -> NUMBER','rhs_expression_list',1,'p_rhs_expression_list__number','',245),
  ('rhs_expression_list -> rhs_expression_list COMMA rhs_expression_list','rhs_expression_list',3,'p_rhs_expression_list','',249),
  ('appl_args -> appl','appl_args',1,'p_appl_args__appl__record','',256),
  ('appl_args -> record','appl_args',1,'p_appl_args__appl__record','',257),
  ('appl_args -> ( rhs_expression )','appl_args',3,'p_appl_args__rhs_expression','',261),
  ('appl_args -> NAME','appl_args',1,'p_appl_args__name','',265),
  ('appl_args -> BIT','appl_args',1,'p_appl_args__bit','',269),
  ('appl_args -> NUMBER','appl_args',1,'p_appl_args__number','',273),
  ('appl_args -> STRING','appl_args',1,'p_appl_args__string','',277),
  ('appl_args -> appl_args COMMA appl_args','appl_args',3,'p_appl_args','',281),
  ('appl -> NAME ( appl_args )','appl',4,'p_appl','',288),
  ('appl -> BIT ( appl_args )','appl',4,'p_appl','',289),
  ('record -> LBRACE record_opt RBRACE','record',3,'p_record','',300),
  ('record_opt -> record_opt SEMI record_opt','record_opt',3,'p_record_opt1','',304),
  ('record_opt -> record_item','record_opt',1,'p_record_opt2','',308),
  ('record_opt -> empty','record_opt',1,'p_record_opt3','',312),
  ('record_name -> NAME','record_name',1,'p_record_name','',316),
  ('record_name -> BIT','record_name',1,'p_record_name','',317),
  ('record_name -> TYPE','record_name',1,'p_record_name','',318),
  ('record_item -> record_name COLON ( rhs_expression )','record_item',5,'p_record_item1','',322),
  ('record_item -> record_name COLON rhs_expression','record_item',3,'p_record_item2','',326),
  ('empty -> <empty>','empty',0,'p_empty','',332),
]