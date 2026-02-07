/**
 * LineChart Component - For displaying timeline data
 */
import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

const LineChart = ({ data, title, yAxisLabel, color = '#6366F1' }) => {
  const chartData = {
    labels: data.labels,
    datasets: [
      {
        label: yAxisLabel,
        data: data.values,
        borderColor: color,
        backgroundColor: `${color}20`,
        fill: true,
        tension: 0.4,
        pointRadius: 4,
        pointBackgroundColor: color,
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
        pointHoverRadius: 6,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: title,
        font: {
          size: 16,
          weight: '600',
          family: 'Bricolage Grotesque, sans-serif',
        },
        color: '#1F2937',
        padding: {
          bottom: 20,
        },
      },
      tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        padding: 12,
        titleFont: {
          size: 13,
          family: 'DM Mono, monospace',
        },
        bodyFont: {
          size: 14,
          family: 'Bricolage Grotesque, sans-serif',
        },
        displayColors: false,
        callbacks: {
          label: function(context) {
            let label = context.dataset.label || '';
            if (label) {
              label += ': ';
            }
            label += context.parsed.y.toFixed(2);
            if (yAxisLabel.includes('%') || yAxisLabel.includes('Gap')) {
              label += '%';
            }
            return label;
          }
        }
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        grid: {
          color: 'rgba(0, 0, 0, 0.05)',
        },
        ticks: {
          font: {
            family: 'DM Mono, monospace',
            size: 11,
          },
          color: '#6B7280',
          callback: function(value) {
            return value.toFixed(1);
          }
        },
        title: {
          display: true,
          text: yAxisLabel,
          font: {
            family: 'Bricolage Grotesque, sans-serif',
            size: 12,
            weight: '600',
          },
          color: '#4B5563',
        }
      },
      x: {
        grid: {
          color: 'rgba(0, 0, 0, 0.05)',
        },
        ticks: {
          font: {
            family: 'DM Mono, monospace',
            size: 11,
          },
          color: '#6B7280',
        },
        title: {
          display: true,
          text: 'Year',
          font: {
            family: 'Bricolage Grotesque, sans-serif',
            size: 12,
            weight: '600',
          },
          color: '#4B5563',
        }
      },
    },
  };

  return (
    <div style={{ height: '300px', width: '100%' }}>
      <Line data={chartData} options={options} />
    </div>
  );
};

export default LineChart;