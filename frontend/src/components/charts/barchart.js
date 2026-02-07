/**
 * BarChart Component - For comparing metrics
 */
import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const BarChart = ({ data, title, yAxisLabel, color = '#8B5CF6' }) => {
  const chartData = {
    labels: data.labels,
    datasets: [
      {
        label: yAxisLabel,
        data: data.values,
        backgroundColor: `${color}90`,
        borderColor: color,
        borderWidth: 2,
        borderRadius: 6,
        hoverBackgroundColor: color,
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
            label += context.parsed.y.toFixed(3);
            return label;
          }
        }
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        min: 0.75,
        max: 1.0,
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
            return value.toFixed(2);
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
          display: false,
        },
        ticks: {
          font: {
            family: 'DM Mono, monospace',
            size: 11,
          },
          color: '#6B7280',
        },
      },
    },
  };

  return (
    <div style={{ height: '300px', width: '100%' }}>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default BarChart;