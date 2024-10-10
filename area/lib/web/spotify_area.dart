import 'package:area/web/web_nav_bar.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

class SpotifyPage extends StatelessWidget {
  const SpotifyPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const WebNavBar(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _buildContainer(context, 'Action', const Color.fromRGBO(29, 185, 84, 1)),
                _buildContainer(context, 'Reaction', Colors.red),
              ],
            ),
            const SizedBox(height: 40), // Increase the space between the rows
            ElevatedButton(
              onPressed: () {
                if (kDebugMode) {
                  print('Button pressed');
                }
              },
              child: const Text('Action Button'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildContainer(BuildContext context, String title, Color color) {
    return Container(
      width: 300, // Increase the width of the container
      height: 150, // Increase the height of the container
      padding: const EdgeInsets.all(20.0),
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(10),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 10,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            title,
            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
          ),
          const SizedBox(height: 10),
          DropdownButton<String>(
            items: <String>['Option 1', 'Option 2', 'Option 3'].map((String value) {
              return DropdownMenuItem<String>(
                value: value,
                child: Text(value),
              );
            }).toList(),
            onChanged: (_) {},
            hint: const Text('Select an option', style: TextStyle(color: Colors.white)),
            dropdownColor: color,
          ),
        ],
      ),
    );
  }
}