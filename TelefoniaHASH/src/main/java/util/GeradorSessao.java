/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package util;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.UUID;

/**
 *
 * @author laboratorio
 */
public class GeradorSessao {
    
    private static final Random random = new Random();
    
    // Arrays para variar os dados
    private static final String[] BEARERS = {"LTE", "5G", "4G", "3G", "UMTS"};
    private static final String[] CODECS = {"AMR-WB", "EVS", "AMR-NB", "G.711", "OPUS"};
    private static final String[] ENCRYPTIONS = {"SRTP", "TLS", "DTLS", "IPSec"};
    private static final String[] MCCS = {"724", "310", "262", "208", "234"}; // Brasil, EUA, Alemanha, França, UK
    
    public static void main(String[] args) {
        String fileName = "telephony_sessions.txt";
        int totalRecords = 1_000_000;
        
        System.out.println("Iniciando geração de " + totalRecords + " registros...");
        System.out.println("Arquivo: " + fileName);
        System.out.println();
        
        long startTime = System.currentTimeMillis();
        
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            
            // Primeiro registro
            writer.write("5591999123456;{\"session_id\":\"uuid\",\"imsi\":\"123456789012345\",\"imei\":\"356789012345678\",\"mcc\":\"724\",\"mnc\":\"01\",\"cell_id\":12345,\"lac\":54321,\"bearer\":\"LTE\",\"start_time\":\"2025-11-05T12:34:56Z\",\"end_time\":\"2025-11-05T12:45:10Z\",\"duration_s\":614,\"ip_addr\":\"10.23.5.6\",\"sip_call_id\":\"uuid2\",\"codec\":\"AMR-WB\",\"bytes_up\":12345,\"bytes_down\":456789,\"lat\":-23.550520,\"lon\":-46.633308,\"encryption\":\"SRTP\"}");
            writer.newLine();
            
            // Gera os outros 999.999 registros
            for (int i = 2; i <= totalRecords; i++) {
                String record = generateRecord(i);
                writer.write(record);
                writer.newLine();
                
                // Mostra progresso a cada 50.000 registros
                if (i % 50_000 == 0) {
                    double progress = (i * 100.0) / totalRecords;
                    System.out.printf("Progresso: %.1f%% (%d/%d registros)%n", progress, i, totalRecords);
                }
            }
            
            long endTime = System.currentTimeMillis();
            long duration = (endTime - startTime) / 1000;
            
            System.out.println();
            System.out.println("Arquivo gerado com sucesso!");
            System.out.println("Total de registros: " + totalRecords);
            System.out.println("Tempo total: " + duration + " segundos");
            System.out.println("Arquivo: " + fileName);
            
        } catch (IOException e) {
            System.err.println("Erro ao gerar arquivo: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Gera um registro de sessão telefônica
     */
    private static String generateRecord(int index) {
        // Gera número de celular brasileiro (55 + DDD + número)
        String phoneNumber = generatePhoneNumber();
        
        // Gera os dados da sessão em formato JSON
        String sessionData = generateSessionData(index);
        
        return phoneNumber + ";" + sessionData;
    }
    
    /**
     * Gera um número de celular brasileiro aleatório
     */
    private static String generatePhoneNumber() {
        // Código do país: 55 (Brasil)
        String countryCode = "55";
        
        // DDD (11 a 99)
        int ddd = random.nextInt(89) + 11;
        
        // Número de celular: 9 + 8 dígitos
        String number = "9" + String.format("%08d", random.nextInt(100_000_000));
        
        return countryCode + ddd + number;
    }
    
    /**
     * Gera os dados da sessão em formato JSON
     */
    private static String generateSessionData(int index) {
        String sessionId = UUID.randomUUID().toString();
        String imsi = String.format("%015d", random.nextLong() & Long.MAX_VALUE).substring(0, 15);
        String imei = String.format("%015d", random.nextLong() & Long.MAX_VALUE).substring(0, 15);
        
        String mcc = MCCS[random.nextInt(MCCS.length)];
        String mnc = String.format("%02d", random.nextInt(100));
        
        int cellId = random.nextInt(99999) + 1;
        int lac = random.nextInt(99999) + 1;
        
        String bearer = BEARERS[random.nextInt(BEARERS.length)];
        
        // Gera timestamps aleatórios
        String startTime = generateTimestamp();
        int durationSeconds = random.nextInt(3600) + 60; // 1min a 1hora
        String endTime = generateTimestamp(); // Simplificado
        
        // IP aleatório
        String ipAddr = String.format("10.%d.%d.%d", 
            random.nextInt(256),
            random.nextInt(256),
            random.nextInt(256));
        
        String sipCallId = UUID.randomUUID().toString();
        String codec = CODECS[random.nextInt(CODECS.length)];
        
        int bytesUp = random.nextInt(1_000_000) + 1000;
        int bytesDown = random.nextInt(10_000_000) + 10000;
        
        // Coordenadas aleatórias do Brasil
        double lat = -30.0 + (random.nextDouble() * 25.0); // -30 a -5
        double lon = -73.0 + (random.nextDouble() * 30.0); // -73 a -43
        
        String encryption = ENCRYPTIONS[random.nextInt(ENCRYPTIONS.length)];
        
        // Monta o JSON (em uma linha)
        return String.format(
            "{\"session_id\":\"%s\",\"imsi\":\"%s\",\"imei\":\"%s\",\"mcc\":\"%s\",\"mnc\":\"%s\"," +
            "\"cell_id\":%d,\"lac\":%d,\"bearer\":\"%s\",\"start_time\":\"%s\",\"end_time\":\"%s\"," +
            "\"duration_s\":%d,\"ip_addr\":\"%s\",\"sip_call_id\":\"%s\",\"codec\":\"%s\"," +
            "\"bytes_up\":%d,\"bytes_down\":%d,\"lat\":%.6f,\"lon\":%.6f,\"encryption\":\"%s\"}",
            sessionId, imsi, imei, mcc, mnc, cellId, lac, bearer, startTime, endTime,
            durationSeconds, ipAddr, sipCallId, codec, bytesUp, bytesDown, lat, lon, encryption
        );
    }
    
    /**
     * Gera um timestamp aleatório
     */
    private static String generateTimestamp() {
        int year = 2025;
        int month = random.nextInt(12) + 1;
        int day = random.nextInt(28) + 1; // Simplificado
        int hour = random.nextInt(24);
        int minute = random.nextInt(60);
        int second = random.nextInt(60);
        
        return String.format("%04d-%02d-%02dT%02d:%02d:%02dZ",
            year, month, day, hour, minute, second);
    }
    
}
