import 'package:flutter/material.dart';

class VehicleCard extends StatelessWidget {
  final String vin;
  final String manufacturer;
  final String model;
  final int year;
  final String? color;
  final VoidCallback onTap;

  const VehicleCard({
    Key? key,
    required this.vin,
    required this.manufacturer,
    required this.model,
    required this.year,
    this.color,
    required this.onTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Card(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    '$manufacturer $model',
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                  Text(
                    year.toString(),
                    style: Theme.of(context).textTheme.bodySmall,
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                'VIN: $vin',
                style: Theme.of(context).textTheme.bodySmall,
              ),
              if (color != null) ...
                [
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Container(
                        width: 20,
                        height: 20,
                        decoration: BoxDecoration(
                          color: Colors.grey,
                          borderRadius: BorderRadius.circular(4),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        color!,
                        style: Theme.of(context).textTheme.bodySmall,
                      ),
                    ],
                  ),
                ],
            ],
          ),
        ),
      ),
    );
  }
}
