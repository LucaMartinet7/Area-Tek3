import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../shared/service_box.dart';
import 'web_nav_bar.dart';

class Service {
  final String name;
  final String logoPath;
  final bool isConnected;

  Service(this.name, this.logoPath, this.isConnected);
}

class UserProfile {
  final String username;
  final String email;
  final String profileImagePath;

  UserProfile({required this.username, required this.email, required this.profileImagePath});

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      username: json['username'],
      email: json['email'],
      profileImagePath: json['profile_image'] ?? 'assets/images/profile/profile.png',
    );
  }
}

class WebDashboard extends StatelessWidget {
  const WebDashboard({super.key});

  Future<UserProfile> fetchUserProfile() async {
    final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/auth/dj-rest-auth/user/'));

    if (response.statusCode == 200) {
      return UserProfile.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to load user profile');
    }
  }

  @override
  Widget build(BuildContext context) {
    final services = [
      Service('Spotify', 'assets/images/spotify.png', true),
      Service('Twitch', 'assets/images/twitch.png', false),
      Service('Google', 'assets/images/google.png', true),
      Service('Microsoft', 'assets/images/microsoft.png', true),
    ];

    void handleConnect(String serviceName) {
      if (kDebugMode) {
        print('Connecting to $serviceName');
      }
    }

    return Scaffold(
      appBar: const WebNavBar(),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              _buildProfile(),
              const SizedBox(width: 16),
              _buildServiceBoxes(services, handleConnect),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildProfile() {
    return Expanded(
      flex: 1,
      child: Container(
        padding: const EdgeInsets.all(16.0),
        decoration: _boxDecoration(),
        child: FutureBuilder<UserProfile>(
          future: fetchUserProfile(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return _buildProfileContent(
                CircleAvatar(
                  radius: 50,
                  child: const Icon(Icons.person, size: 50),
                ),
                'Error',
                'error@example.com',
              );
            } else if (!snapshot.hasData) {
              return _buildProfileContent(
                CircleAvatar(
                  radius: 50,
                  child: const Icon(Icons.person, size: 50),
                ),
                'No Data',
                'nodata@example.com',
              );
            } else {
              final userProfile = snapshot.data!;
              return _buildProfileContent(
                CircleAvatar(
                  radius: 50,
                  backgroundImage: NetworkImage(userProfile.profileImagePath),
                ),
                userProfile.username,
                userProfile.email,
              );
            }
          },
        ),
      ),
    );
  }

  Widget _buildProfileContent(Widget avatar, String username, String email) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        avatar,
        const SizedBox(height: 10),
        Text(
          username,
          style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 5),
        Text(
          email,
          style: const TextStyle(fontSize: 16, color: Colors.grey),
        ),
      ],
    );
  }

  Widget _buildServiceBoxes(
      List<Service> services, void Function(String) handleConnect) {
    return Expanded(
      flex: 1,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: services
            .map((service) => ServiceBox(
                  logoPath: service.logoPath,
                  isConnected: service.isConnected,
                  onConnect: () => handleConnect(service.name),
                  serviceName: service.name,
                ))
            .toList(),
      ),
    );
  }

  BoxDecoration _boxDecoration() {
    return BoxDecoration(
      color: Colors.white,
      borderRadius: BorderRadius.circular(10),
      boxShadow: [
        BoxShadow(
          color: Colors.grey.withOpacity(0.5),
          spreadRadius: 2,
          blurRadius: 5,
          offset: const Offset(0, 3),
        ),
      ],
    );
  }
}