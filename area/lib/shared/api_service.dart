import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

Future<http.Response> postRequest({
  required String url,
  required Map<String, String> headers,
  required Map<String, dynamic> body,
}) async {
  final response = await http.post(
    Uri.parse(url),
    headers: headers,
    body: jsonEncode(body),
  );
  return response;
}

Future<void> login({
  required BuildContext context,
  required String username,
  required String password,
}) async {
  final response = await postRequest(
    url: 'http://127.0.0.1:8000/api/auth/login/',
    headers: {'Content-Type': 'application/json'},
    body: {
      'username': username,
      'password': password,
    },
  );

  if (!context.mounted) return;

  if (response.statusCode == 200) {
    Navigator.pushNamed(context, '/dashboard');
  } else {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Login failed: ${response.statusCode}')),
    );
  }
}

Future<void> register({
  required BuildContext context,
  required String username,
  required String password,
  required String email,
}) async {
  final response = await postRequest(
    url: 'http://127.0.0.1:8000/api/auth/register/',
    headers: {'Content-Type': 'application/json'},
    body: {
      'username': username,
      'password': password,
      'email': email,
      'first_name': 'none',
      'last_name': 'none',
    },
  );

  if (!context.mounted) return;

  if (response.statusCode == 200) {
    Navigator.pushNamed(context, '/login');
  } else {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Registration failed: ${response.statusCode}')),
    );
  }
}

Future<void> launchURL(String url) async {
    final Uri uri = Uri.parse(url);
    if (!await launchUrl(uri, mode: LaunchMode.externalApplication)) {
      throw 'Could not launch $url';
    }
  }

Future<List<String>> fetchActions() async {
  final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/actions/'));

  if (response.statusCode == 200) {
    List<dynamic> data = json.decode(response.body);
    return data.map((action) => action.toString()).toList();
  } else {
    throw Exception('Failed to load actions');
  }
}

Future<List<String>> fetchReactions() async {
  final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/reactions/'));

  if (response.statusCode == 200) {
    List<dynamic> data = json.decode(response.body);
    return data.map((reaction) => reaction.toString()).toList();
  } else {
    throw Exception('Failed to load reactions');
  }
}