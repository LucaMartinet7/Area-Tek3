import 'package:flutter/material.dart';

class ServiceNameBox extends StatelessWidget {
  final String logoPath;
  final VoidCallback onConnect;
  final List<Color> backgroundColors;

  const ServiceNameBox({
    required this.logoPath,
    required this.onConnect,
    required this.backgroundColors,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(8.0),
      height: 150,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(10.0),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset(
                logoPath,
                height: 40,
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Row(
                  children: backgroundColors.map((color) {
                    return Expanded(
                      child: Container(
                        height: 40,
                        color: color,
                      ),
                    );
                  }).toList(),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          GestureDetector(
            onTap: onConnect,
            child: const Text(
              'Connect',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
          ),
        ],
      ),
    );
  }
}