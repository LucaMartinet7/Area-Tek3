import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:tuple/tuple.dart';
import '../web/web_nav_bar.dart';

class ActionReactionPage extends StatelessWidget {
    final String title;
    final List<String> actions;
    final List<Tuple2<String, String>> reactions;

    const ActionReactionPage({
        required this.title,
        required this.actions,
        required this.reactions,
        super.key,
    });

    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: const WebNavBar(),
            body: Column(
                children: [
                    Expanded(
                        child: GridView.builder(
                            padding: const EdgeInsets.all(50.0),
                            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                                crossAxisCount: 5,
                                crossAxisSpacing: 15.0,
                                mainAxisSpacing: 15.0,
                                childAspectRatio: 3 / 4,
                            ),
                            itemCount: actions.length,
                            itemBuilder: (context, index) {
                                return ActionReactionRectangle(
                                    action: actions[index],
                                    reactions: reactions,
                                    color: Colors.primaries[index % Colors.primaries.length].shade700,
                                );
                            },
                        ),
                    ),
                ],
            ),
        );
    }
}

class ActionReactionRectangle extends StatefulWidget {
    final String action;
    final List<Tuple2<String, String>> reactions;
    final Color color;

    const ActionReactionRectangle({
        required this.action,
        required this.reactions,
        required this.color,
        super.key,
    });

    @override
    ActionReactionRectangleState createState() => ActionReactionRectangleState();
}

class ActionReactionRectangleState extends State<ActionReactionRectangle> {
    bool _hovering = false;
    bool _isActive = false;
    String? _selectedReaction;

    @override
    Widget build(BuildContext context) {
        return GestureDetector(
            onTap: _handleTap,
            child: MouseRegion(
                onEnter: (_) => setState(() => _hovering = true),
                onExit: (_) => setState(() => _hovering = false),
                child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    decoration: BoxDecoration(
                        color: _hovering ? widget.color.withOpacity(0.7) : widget.color,
                        borderRadius: BorderRadius.circular(10),
                    ),
                    child: Center(
                        child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                                _buildActionText(),
                                _buildReactionDropdown(),
                                _buildSwitch(),
                            ],
                        ),
                    ),
                ),
            ),
        );
    }

    void _handleTap() {
        if (kDebugMode) {
            print('Action: ${widget.action}, Reaction: $_selectedReaction');
        }
    }

    Widget _buildActionText() {
        return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Text(
                widget.action,
                textAlign: TextAlign.center,
                overflow: TextOverflow.ellipsis,
                maxLines: 2,
                style: const TextStyle(fontSize: 20, color: Colors.white),
            ),
        );
    }

    Widget _buildReactionDropdown() {
        return SizedBox(
            width: 200,
            child: DropdownButtonHideUnderline(
                child: DropdownButton<String>(
                    value: _selectedReaction,
                    hint: const Text('Select Reaction', style: TextStyle(color: Colors.white)),
                    dropdownColor: widget.color,
                    isExpanded: true,
                    items: _buildDropdownMenuItems(),
                    onChanged: (value) {
                        setState(() {
                            _selectedReaction = value;
                        });
                    },
                    selectedItemBuilder: (BuildContext context) {
                        return _buildSelectedItems();
                    },
                ),
            ),
        );
    }

    List<DropdownMenuItem<String>> _buildDropdownMenuItems() {
        return widget.reactions.map((reaction) {
            return DropdownMenuItem<String>(
                value: '${reaction.item1}: ${reaction.item2}',
                child: RichText(
                    text: TextSpan(
                        children: [
                            TextSpan(
                                text: '${reaction.item1}: ',
                                style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.white),
                            ),
                            TextSpan(
                                text: reaction.item2,
                                style: const TextStyle(fontSize: 14, color: Colors.white),
                            ),
                        ],
                    ),
                ),
            );
        }).toList();
    }

    List<Widget> _buildSelectedItems() {
        return widget.reactions.map<Widget>((reaction) {
            return Text(
                '${reaction.item1}: ${reaction.item2}',
                style: const TextStyle(color: Colors.white),
            );
        }).toList();
    }

    Widget _buildSwitch() {
        return Switch(
            value: _isActive,
            onChanged: _selectedReaction == null ? null : (value) {
                setState(() {
                    _isActive = value;
                });
            },
        );
    }
}