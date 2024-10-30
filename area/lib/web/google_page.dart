import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import 'area_page.dart';

class GooglePage extends StatelessWidget {
  const GooglePage({super.key});

  static const List<Tuple2<String, String>> list = [
    Tuple2('Test Action', 'Test Reaction'),
  ];

  @override
  Widget build(BuildContext context) {
    return ActionReactionPage(
      title: 'Google',
      area : list
    );
  }
}